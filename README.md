# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_19:17:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 19:17:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-11-27 19:17:42 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-11-27 19:13:06 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-11-27 19:10:59 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-27 19:08:57 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-11-27 19:08:26 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-11-27 19:08:04 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.040 |  |
| 2026-11-27 19:07:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.055 |  |
| 2026-11-27 19:06:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-11-27 19:06:34 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-27 19:06:33 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-11-27 19:06:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.086 |  |
| 2026-11-27 19:05:35 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-11-27 19:05:31 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-11-27 19:05:26 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.097 |  |
| 2026-11-27 19:05:16 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.081 |  |
| 2026-11-27 19:04:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 19:04:28 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-27 19:04:24 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.048 |  |
| 2026-11-27 19:04:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.068 |  |
| 2026-11-27 19:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 19:04:10 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-27 19:03:44 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.049 |  |
| 2026-11-27 19:03:33 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:03:24 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.071 |  |
| 2026-11-27 19:02:47 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.228 |  |
| 2026-11-27 19:02:40 | Moraketiya (Walawe Ganga) | 3.42 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-11-27 19:02:39 | Magura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.101 |  |
| 2026-11-27 19:02:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:02:28 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-27 19:02:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-27 19:01:36 | Wellawaya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.199 |  |
| 2026-11-27 19:01:31 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-11-27 19:01:28 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-27 19:00:59 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 19:02:40 | Moraketiya (Walawe Ganga) | 3.42 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-11-27 19:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 19:04:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.068 |  |
| 2026-11-27 19:17:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-11-27 19:08:26 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-11-27 19:06:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-11-27 19:05:35 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-11-27 19:05:31 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-11-27 19:04:10 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-27 19:06:34 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-27 19:04:28 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-27 19:10:59 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-27 19:04:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 19:02:28 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-27 19:02:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:03:33 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:02:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-27 19:08:57 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-11-27 19:00:59 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-11-27 19:06:33 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-11-27 19:01:28 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 19:13:06 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-11-27 19:08:04 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:01:29 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-27 19:04:24 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.048 |  |
| 2026-11-27 19:03:44 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.049 |  |
| 2026-11-27 19:07:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.055 |  |
| 2026-11-27 19:03:24 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.071 |  |
| 2026-11-27 19:05:16 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.081 |  |
| 2026-11-27 19:06:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.086 |  |
| 2026-11-27 19:05:26 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.097 |  |
| 2026-11-27 19:01:31 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.099 |  |
| 2026-11-27 19:02:39 | Magura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.101 |  |
| 2026-11-27 19:01:36 | Wellawaya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.199 |  |
| 2026-11-27 19:02:47 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)