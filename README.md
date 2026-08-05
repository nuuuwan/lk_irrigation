# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_18:01:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:00 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-08-05 18:00:46 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:00:09 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-08-05 17:13:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 17:03:29 | Peradeniya (Mahaweli Ganga) | 6.38 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-08-05 17:01:17 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-05 17:02:09 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-05 17:02:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-05 17:02:24 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 17:06:51 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-05 17:07:38 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 17:00:49 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-05 17:01:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:00:20 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:04:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:03:30 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:13:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:04:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:03:49 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:03:23 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:04:29 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:01:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:00:54 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:00:46 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 17:02:34 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 17:04:42 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:00:09 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-08-05 17:08:03 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.015 |  |
| 2026-08-05 17:07:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-08-05 17:06:19 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-08-05 17:04:09 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.033 |  |
| 2026-08-05 17:04:35 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.045 |  |
| 2026-08-05 17:04:50 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.047 |  |
| 2026-08-05 17:03:02 | Ellagawa (Kalu Ganga) | 8.74 | 🟢 Normal | -0.049 |  |
| 2026-08-05 17:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | -0.050 |  |
| 2026-08-05 17:03:08 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.050 |  |
| 2026-08-05 18:01:00 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-08-05 17:02:32 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.061 |  |
| 2026-08-05 17:03:58 | Glencourse (Kelani Ganga) | 12.21 | 🟢 Normal | -0.063 |  |
| 2026-08-05 17:11:21 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)