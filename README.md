# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_11:15:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,939 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 11:15:49 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.516 |  |
| 2026-11-10 11:12:38 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.081 |  |
| 2026-11-10 11:11:31 | Magura (Kalu Ganga) | 4.89 | 🟡 Alert | -0.074 |  |
| 2026-11-10 11:10:05 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-10 11:09:29 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 11:09:05 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-10 11:08:17 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-11-10 11:08:04 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.247 |  |
| 2026-11-10 11:07:17 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | -0.055 |  |
| 2026-11-10 11:07:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.057 |  |
| 2026-11-10 11:06:41 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:06:40 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-10 11:06:16 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 11:05:46 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | -0.096 |  |
| 2026-11-10 11:04:43 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.029 |  |
| 2026-11-10 11:04:31 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.157 |  |
| 2026-11-10 11:03:46 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.139 |  |
| 2026-11-10 11:03:36 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.226 |  |
| 2026-11-10 11:03:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 11:03:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:03:06 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:58 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-11-10 11:02:41 | Moraketiya (Walawe Ganga) | 2.95 | 🟢 Normal | -0.039 |  |
| 2026-11-10 11:02:37 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.088 |  |
| 2026-11-10 11:02:33 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 11:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-10 11:02:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 11:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:01:35 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-10 11:01:25 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-10 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-10 11:00:49 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-10 11:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 11:09:29 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 11:06:16 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 10:08:36 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 11:07:17 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | -0.055 |  |
| 2026-11-10 11:11:31 | Magura (Kalu Ganga) | 4.89 | 🟡 Alert | -0.074 |  |
| 2026-11-10 11:01:25 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-10 11:02:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-10 11:06:40 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-10 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-10 11:01:35 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-10 11:03:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 10:10:36 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:03:06 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:06:41 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:08:17 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-11-10 11:10:05 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-10 11:03:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:00:49 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:02:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 11:09:05 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-10 11:02:33 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:02:58 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-11-10 11:04:43 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.029 |  |
| 2026-11-10 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-10 11:02:41 | Moraketiya (Walawe Ganga) | 2.95 | 🟢 Normal | -0.039 |  |
| 2026-11-10 11:07:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.057 |  |
| 2026-11-10 11:12:38 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | -0.081 |  |
| 2026-11-10 11:02:37 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.088 |  |
| 2026-11-10 11:05:46 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | -0.096 |  |
| 2026-11-10 11:03:46 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.139 |  |
| 2026-11-10 11:04:31 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.157 |  |
| 2026-11-10 11:03:36 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.226 |  |
| 2026-11-10 11:08:04 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.247 |  |
| 2026-11-10 11:15:49 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.516 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)