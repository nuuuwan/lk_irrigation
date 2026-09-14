# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_02:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,138 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thawalama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 02:03:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 02:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:02:34 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.152 | 🔺 Rising |
| 2026-09-15 02:02:23 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 02:01:49 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.161 |  |
| 2026-09-15 02:01:48 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:36 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 02:00:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.062 |  |
| 2026-09-15 01:40:40 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:22:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-15 01:19:31 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 01:04:07 | Thawalama (Gin Ganga) | 4.06 | 🟡 Alert | 0.705 | 🔺 Rising |
| 2026-09-15 02:02:34 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.152 | 🔺 Rising |
| 2026-09-15 01:05:27 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 414.000 | 🔺 Rising |
| 2026-09-15 01:03:05 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.727 | 🔺 Rising |
| 2026-09-15 01:12:59 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-09-15 01:06:02 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-09-15 02:02:23 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 01:01:54 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-15 01:22:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-15 01:07:10 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-15 01:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 02:03:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 01:04:26 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-15 00:03:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:48 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:07:58 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:36 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:06:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:03:37 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:06:32 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 01:05:20 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-15 01:04:54 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-09-15 01:02:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-09-15 01:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-15 02:00:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.062 |  |
| 2026-09-15 02:01:49 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.161 |  |
| 2026-09-15 01:01:51 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.330 |  |
| 2026-09-14 23:40:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)