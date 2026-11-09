# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_15:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 15:09:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.036 |  |
| 2026-11-09 15:09:00 | Baddegama (Gin Ganga) | 3.62 | 🟡 Alert | -0.011 |  |
| 2026-11-09 15:06:51 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.060 |  |
| 2026-11-09 15:05:58 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-11-09 15:05:41 | Magura (Kalu Ganga) | 4.64 | 🟡 Alert | -0.073 |  |
| 2026-11-09 15:05:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-09 15:05:01 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-09 15:04:49 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.049 |  |
| 2026-11-09 15:04:45 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-11-09 15:04:41 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 15:04:36 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.080 |  |
| 2026-11-09 15:04:15 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.142 |  |
| 2026-11-09 15:04:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-09 15:04:00 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:03:41 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-11-09 15:03:31 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-11-09 15:03:29 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:03:21 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-09 15:03:19 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.113 |  |
| 2026-11-09 15:03:07 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-09 15:03:04 | Panadugama (Nilwala Ganga) | 5.49 | 🟡 Alert | -0.051 |  |
| 2026-11-09 15:03:01 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 15:02:55 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-09 15:02:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-09 15:02:55 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:02:48 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:02:47 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:02:42 | Moragaswewa (Deduru Oya) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-11-09 15:02:41 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:02:39 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.051 |  |
| 2026-11-09 15:02:36 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | -0.099 |  |
| 2026-11-09 15:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-09 15:01:51 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 15:01:07 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-11-09 15:00:40 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.172 |  |
| 2026-11-09 15:00:39 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:00:10 | Thalgahagoda (Nilwala Ganga) | 1.57 | 🟡 Alert | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 15:03:21 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-09 15:00:10 | Thalgahagoda (Nilwala Ganga) | 1.57 | 🟡 Alert | 0.058 | 🔺 Rising |
| 2026-11-09 15:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 15:09:00 | Baddegama (Gin Ganga) | 3.62 | 🟡 Alert | -0.011 |  |
| 2026-11-09 15:03:04 | Panadugama (Nilwala Ganga) | 5.49 | 🟡 Alert | -0.051 |  |
| 2026-11-09 15:05:41 | Magura (Kalu Ganga) | 4.64 | 🟡 Alert | -0.073 |  |
| 2026-11-09 15:03:31 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-11-09 15:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-09 15:05:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-09 15:04:14 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-09 15:03:07 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-09 15:02:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-09 15:02:55 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-09 15:03:01 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 15:04:41 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 15:05:01 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-09 15:02:48 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:03:29 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:02:47 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:02:55 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:04:00 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 15:05:58 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-11-09 15:02:41 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:01:51 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:00:39 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-09 15:02:42 | Moragaswewa (Deduru Oya) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-11-09 15:03:41 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-11-09 15:04:45 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-11-09 15:09:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.036 |  |
| 2026-11-09 15:01:07 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-11-09 15:04:49 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.049 |  |
| 2026-11-09 15:02:39 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.051 |  |
| 2026-11-09 15:06:51 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.060 |  |
| 2026-11-09 15:04:36 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.080 |  |
| 2026-11-09 15:02:36 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | -0.099 |  |
| 2026-11-09 15:03:19 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.113 |  |
| 2026-11-09 15:04:15 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.142 |  |
| 2026-11-09 15:00:40 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)