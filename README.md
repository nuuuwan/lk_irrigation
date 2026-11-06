# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_03:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 03:02:48 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-11-07 03:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:42 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:35 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.053 |  |
| 2026-11-07 03:02:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-07 03:02:06 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 03:02:01 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-07 03:01:54 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-07 03:01:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.584 |  |
| 2026-11-07 03:01:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-07 03:00:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.072 |  |
| 2026-11-07 02:56:24 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.584 |  |
| 2026-11-07 02:55:53 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 02:49:59 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 01:06:26 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.171 | 🔺 Rising |
| 2026-11-07 02:00:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 02:02:22 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-11-07 02:10:41 | Giriulla (Maha Oya) | 3.43 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 02:02:13 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-07 03:02:01 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-07 03:02:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-07 03:01:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 02:49:59 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-07 02:11:07 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 02:04:44 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 03:02:06 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 02:12:05 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-07 02:55:53 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 01:09:20 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 02:00:25 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:42 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:05:51 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:03:06 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:06:08 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:03:22 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:08:56 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:01:54 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 03:02:48 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-11-07 02:02:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-07 03:02:35 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.053 |  |
| 2026-11-07 03:00:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.072 |  |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 02:03:59 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.087 |  |
| 2026-11-07 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.098 |  |
| 2026-11-07 02:07:18 | Holombuwa (Kelani Ganga) | 2.82 | 🟢 Normal | -0.515 |  |
| 2026-11-07 03:01:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.584 |  |
| 2026-11-07 02:10:21 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)