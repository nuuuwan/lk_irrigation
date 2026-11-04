# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_14:02:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 14:02:35 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.119 |  |
| 2026-11-04 14:01:52 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:48 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.122 |  |
| 2026-11-04 14:01:45 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.091 |  |
| 2026-11-04 14:01:40 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.032 |  |
| 2026-11-04 14:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:06 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 14:00:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:00:24 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.050 |  |
| 2026-11-04 13:17:03 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 13:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-11-04 13:05:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-11-04 13:04:47 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-04 13:01:40 | Moragaswewa (Deduru Oya) | 4.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-04 14:00:56 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 13:02:31 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 13:03:53 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 14:01:06 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-04 13:01:08 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 13:02:13 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 13:01:47 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 13:08:39 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 13:07:14 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-11-04 14:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:01:52 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-04 14:02:35 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-04 13:02:29 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-11-04 13:04:51 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-04 14:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-04 13:07:37 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.027 |  |
| 2026-11-04 13:05:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-11-04 13:02:24 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-11-04 14:01:40 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.032 |  |
| 2026-11-04 13:04:56 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.034 |  |
| 2026-11-04 13:06:09 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.037 |  |
| 2026-11-04 13:04:57 | Giriulla (Maha Oya) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-11-04 13:06:07 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.049 |  |
| 2026-11-04 14:00:24 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.050 |  |
| 2026-11-04 13:00:35 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-11-04 13:06:39 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.053 |  |
| 2026-11-04 13:17:03 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.053 |  |
| 2026-11-04 13:03:41 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.069 |  |
| 2026-11-04 13:05:09 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.081 |  |
| 2026-11-04 13:02:22 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.082 |  |
| 2026-11-04 14:01:45 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.091 |  |
| 2026-11-04 14:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.119 |  |
| 2026-11-04 14:01:48 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)