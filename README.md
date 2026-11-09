# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_17:31:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,306 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 17:31:16 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-11-09 17:14:58 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-09 17:12:22 | Panadugama (Nilwala Ganga) | 5.42 | 🟡 Alert | -0.042 |  |
| 2026-11-09 17:09:27 | Magura (Kalu Ganga) | 4.47 | 🟡 Alert | -0.040 |  |
| 2026-11-09 17:08:39 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-09 17:08:37 | Peradeniya (Mahaweli Ganga) | 4.25 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-09 17:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 17:08:06 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-09 17:07:27 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.039 |  |
| 2026-11-09 17:07:24 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-09 17:07:06 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.047 |  |
| 2026-11-09 17:06:32 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 17:05:21 | Deraniyagala (Kelani Ganga) | 2.39 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-11-09 17:05:16 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.031 |  |
| 2026-11-09 17:04:54 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.107 |  |
| 2026-11-09 17:04:47 | Rathnapura (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 17:04:43 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-11-09 17:04:33 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:04:19 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 17:03:43 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-11-09 17:03:40 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-09 17:03:40 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.131 |  |
| 2026-11-09 17:03:32 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-09 17:03:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:03:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:03:18 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-11-09 17:03:04 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.061 |  |
| 2026-11-09 17:02:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-09 17:02:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:02:30 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-09 17:02:27 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-09 17:02:23 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-11-09 17:02:09 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-11-09 17:01:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 17:01:31 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-11-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:00:49 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:00:09 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 17:00:09 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-11-09 17:06:32 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 17:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 17:05:16 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.031 |  |
| 2026-11-09 17:09:27 | Magura (Kalu Ganga) | 4.47 | 🟡 Alert | -0.040 |  |
| 2026-11-09 17:12:22 | Panadugama (Nilwala Ganga) | 5.42 | 🟡 Alert | -0.042 |  |
| 2026-11-09 17:05:21 | Deraniyagala (Kelani Ganga) | 2.39 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-11-09 17:08:37 | Peradeniya (Mahaweli Ganga) | 4.25 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-09 17:03:43 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-11-09 17:02:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-09 17:02:27 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-09 17:03:40 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-09 17:08:06 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-09 17:03:32 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-09 17:07:24 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-09 17:01:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 17:04:19 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 17:04:47 | Rathnapura (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 17:14:58 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:00:49 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:03:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:03:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:31:16 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-11-09 17:08:39 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-09 17:04:33 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:02:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:04:43 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-11-09 17:02:30 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-09 17:02:23 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-11-09 17:01:31 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-11-09 17:03:18 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-11-09 17:07:27 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.039 |  |
| 2026-11-09 17:02:09 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-11-09 17:07:06 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.047 |  |
| 2026-11-09 17:03:04 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.061 |  |
| 2026-11-09 17:04:54 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.107 |  |
| 2026-11-09 17:03:40 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)