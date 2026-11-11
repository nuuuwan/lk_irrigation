# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_19:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,157 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.008 |  |
| 2026-11-11 19:10:35 | Baddegama (Gin Ganga) | 4.08 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-11 19:10:03 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 19:09:07 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.268 | 🔺 Rising |
| 2026-11-11 19:07:40 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 19:07:31 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:03 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 19:06:54 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-11 19:06:52 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-11-11 19:06:21 | Deraniyagala (Kelani Ganga) | 3.32 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-11 19:06:08 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:05:48 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.010 |  |
| 2026-11-11 19:05:40 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:05:21 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-11 19:04:48 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-11-11 19:04:36 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:04:35 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-11 19:04:19 | Holombuwa (Kelani Ganga) | 2.31 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-11 19:03:55 | Peradeniya (Mahaweli Ganga) | 4.46 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-11 19:03:44 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-11 19:03:34 | Moragaswewa (Deduru Oya) | 3.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-11 19:03:30 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-11 19:03:25 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:03:18 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:02:35 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-11 19:02:03 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-11 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |
| 2026-11-11 19:01:45 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-11-11 19:01:40 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.735 | 🔺 Rising |
| 2026-11-11 19:01:31 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:01:09 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-11-11 19:00:24 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 19:07:03 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 19:10:35 | Baddegama (Gin Ganga) | 4.08 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-11 19:01:40 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.735 | 🔺 Rising |
| 2026-11-11 19:09:07 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.268 | 🔺 Rising |
| 2026-11-11 19:03:18 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.008 |  |
| 2026-11-11 19:05:48 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.010 |  |
| 2026-11-11 19:03:44 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-11 19:06:52 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-11-11 19:06:54 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-11 19:03:30 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-11 19:03:55 | Peradeniya (Mahaweli Ganga) | 4.46 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-11 19:06:21 | Deraniyagala (Kelani Ganga) | 3.32 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-11 19:04:19 | Holombuwa (Kelani Ganga) | 2.31 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-11 19:05:21 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-11 19:04:35 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-11 19:02:03 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-11 19:02:35 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-11 19:01:09 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-11 19:03:34 | Moragaswewa (Deduru Oya) | 3.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-11 19:07:40 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 19:01:31 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:03:25 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 18:03:10 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:10:03 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 19:00:24 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:31 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:04:36 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:05:40 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:06:08 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 19:01:45 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-11-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-11-11 19:04:48 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-11-11 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)