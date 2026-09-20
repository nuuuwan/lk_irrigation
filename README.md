# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_14:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Glencourse — Alert; 🟡 Peradeniya — Alert; 🟡 Panadugama — Alert; 🟡 Holombuwa — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 14:13:50 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-09-20 14:11:36 | Peradeniya (Mahaweli Ganga) | 6.94 | 🟡 Alert | 0.278 | 🔺 Rising |
| 2026-09-20 14:08:18 | Rathnapura (Kalu Ganga) | 6.84 | 🟡 Alert | 0.057 | 🔺 Rising |
| 2026-09-20 14:07:29 | Holombuwa (Kelani Ganga) | 3.25 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-09-20 14:06:52 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:06:23 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:06:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:05:52 | Glencourse (Kelani Ganga) | 15.04 | 🟡 Alert | 0.285 | 🔺 Rising |
| 2026-09-20 14:05:29 | Norwood (Kelani Ganga) | 2.21 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-09-20 14:05:20 | Magura (Kalu Ganga) | 5.19 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-09-20 14:05:18 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-20 14:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | 0.096 | 🔺 Rising |
| 2026-09-20 14:04:58 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.192 | 🔺 Rising |
| 2026-09-20 14:04:48 | Hanwella (Kelani Ganga) | 4.72 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-09-20 14:04:39 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-20 14:04:34 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-20 14:04:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:04:00 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-20 14:03:52 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 14:03:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:03:44 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-09-20 14:03:25 | Deraniyagala (Kelani Ganga) | 4.03 | 🟢 Normal | -0.571 |  |
| 2026-09-20 14:03:20 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:03:19 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:02:48 | Nawalapitiya (Mahaweli Ganga) | 3.98 | 🟡 Alert | -0.833 |  |
| 2026-09-20 14:02:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:02:36 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 14:02:20 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:02:12 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-09-20 14:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-20 14:01:48 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | -0.090 |  |
| 2026-09-20 14:01:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 14:01:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:17 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:02 | Thawalama (Gin Ganga) | 5.06 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 14:00:55 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 14:00:47 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-09-20 14:00:39 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.020 |  |
| 2026-09-20 13:59:44 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.110 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 14:05:52 | Glencourse (Kelani Ganga) | 15.04 | 🟡 Alert | 0.285 | 🔺 Rising |
| 2026-09-20 14:11:36 | Peradeniya (Mahaweli Ganga) | 6.94 | 🟡 Alert | 0.278 | 🔺 Rising |
| 2026-09-20 14:04:58 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.192 | 🔺 Rising |
| 2026-09-20 14:07:29 | Holombuwa (Kelani Ganga) | 3.25 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-09-20 14:05:20 | Magura (Kalu Ganga) | 5.19 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-09-20 14:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | 0.096 | 🔺 Rising |
| 2026-09-20 14:01:02 | Thawalama (Gin Ganga) | 5.06 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 14:08:18 | Rathnapura (Kalu Ganga) | 6.84 | 🟡 Alert | 0.057 | 🔺 Rising |
| 2026-09-20 14:05:29 | Norwood (Kelani Ganga) | 2.21 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-09-20 14:02:48 | Nawalapitiya (Mahaweli Ganga) | 3.98 | 🟡 Alert | -0.833 |  |
| 2026-09-20 14:04:48 | Hanwella (Kelani Ganga) | 4.72 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-09-20 14:04:34 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-20 14:03:44 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-09-20 14:13:50 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-09-20 13:59:44 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-20 14:04:39 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-20 14:04:00 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-20 14:05:18 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-20 14:01:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 14:00:55 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 14:03:52 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 14:03:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:04:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:17 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:06:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:06:52 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:01:36 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:03:20 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:02:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:06:23 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:03:19 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 14:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-20 14:02:36 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 14:00:47 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-09-20 14:00:39 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.020 |  |
| 2026-09-20 14:02:12 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-09-20 14:01:48 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | -0.090 |  |
| 2026-09-20 14:03:25 | Deraniyagala (Kelani Ganga) | 4.03 | 🟢 Normal | -0.571 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)