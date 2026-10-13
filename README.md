# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_16:20:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,881 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 16:20:39 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:12:41 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.046 |  |
| 2026-10-13 16:11:36 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.036 |  |
| 2026-10-13 16:11:06 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:10:50 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:09:37 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.063 |  |
| 2026-10-13 16:09:12 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-10-13 16:08:36 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-13 16:08:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-10-13 16:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.019 |  |
| 2026-10-13 16:06:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-10-13 16:06:04 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-13 16:05:49 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.235 |  |
| 2026-10-13 16:05:46 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:05:44 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:05:11 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:05:09 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.038 |  |
| 2026-10-13 16:04:29 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-10-13 16:04:21 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:04:14 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:04:08 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 16:04:03 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:03:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:03:51 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:03:17 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.019 |  |
| 2026-10-13 16:02:54 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 16:02:49 | Thalgahagoda (Nilwala Ganga) | 1.57 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-13 16:02:34 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.055 |  |
| 2026-10-13 16:02:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-13 16:02:07 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:02:01 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:01:14 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:00:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:48 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-10-13 16:00:09 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 16:02:49 | Thalgahagoda (Nilwala Ganga) | 1.57 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-13 16:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.019 |  |
| 2026-10-13 16:02:34 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.055 |  |
| 2026-10-13 16:08:36 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-13 16:06:04 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-13 16:04:08 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 16:02:54 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 16:02:01 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:02:07 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:20:39 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:11:06 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:10:50 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:09:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:04:14 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:03:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:05:46 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:04:21 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:01:14 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 16:08:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-10-13 16:06:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-10-13 16:03:51 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:48 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:05:11 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:00:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:05:44 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:04:03 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-13 16:03:17 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.019 |  |
| 2026-10-13 16:00:09 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-10-13 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-10-13 16:09:12 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-10-13 16:04:29 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-10-13 16:11:36 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.036 |  |
| 2026-10-13 16:05:09 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.038 |  |
| 2026-10-13 16:02:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-13 16:12:41 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.046 |  |
| 2026-10-13 16:09:37 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.063 |  |
| 2026-10-13 16:05:49 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)