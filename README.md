# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_20:16:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,516 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Thawalama — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 20:16:49 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-08 20:14:32 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 20:13:32 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:13:29 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:13:26 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:12:51 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-08 20:09:33 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:09:25 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-11-08 20:09:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:08:31 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-08 20:07:44 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-11-08 20:06:52 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-08 20:06:20 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-11-08 20:06:07 | Peradeniya (Mahaweli Ganga) | 4.34 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-08 20:05:46 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-11-08 20:05:41 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.554 |  |
| 2026-11-08 20:05:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:05:21 | Thaldena (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-08 20:05:10 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-08 20:04:25 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | 0.656 | 🔺 Rising |
| 2026-11-08 20:04:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-08 20:03:55 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-08 20:03:47 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.099 |  |
| 2026-11-08 20:03:23 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:03:12 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2026-11-08 20:03:11 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.212 |  |
| 2026-11-08 20:03:08 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-08 20:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-08 20:02:47 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-08 20:02:43 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:02:42 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:02:11 | Holombuwa (Kelani Ganga) | 3.79 | 🟠 Minor Flood | -0.109 |  |
| 2026-11-08 20:01:41 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:01:30 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 20:00:14 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-11-08 20:00:01 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.478 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 20:02:11 | Holombuwa (Kelani Ganga) | 3.79 | 🟠 Minor Flood | -0.109 |  |
| 2026-11-08 20:04:25 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | 0.656 | 🔺 Rising |
| 2026-11-08 20:03:12 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2026-11-08 20:05:10 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-08 20:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-08 20:00:14 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-11-08 19:05:54 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 20:05:46 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-11-08 20:00:01 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-11-08 20:06:20 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-11-08 20:02:47 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-08 20:02:42 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-08 20:05:21 | Thaldena (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-08 20:06:07 | Peradeniya (Mahaweli Ganga) | 4.34 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-08 20:08:31 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-08 20:03:55 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 20:04:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-08 20:06:52 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-08 20:03:08 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-08 20:01:30 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 20:16:49 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-08 20:14:32 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 20:12:51 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-08 20:05:34 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:03:23 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:09:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:13:32 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:09:33 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:02:43 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 20:09:25 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 20:07:44 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-11-08 20:01:41 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:03:47 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.099 |  |
| 2026-11-08 20:03:11 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.212 |  |
| 2026-11-08 20:05:41 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.554 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)