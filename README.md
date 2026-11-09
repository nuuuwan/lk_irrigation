# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_22:15:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,485 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Peradeniya — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 22:15:05 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:11:00 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.036 |  |
| 2026-11-09 22:10:04 | Thaldena (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.200 |  |
| 2026-11-09 22:09:21 | Holombuwa (Kelani Ganga) | 1.84 | 🟢 Normal | -0.137 |  |
| 2026-11-09 22:08:46 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-11-09 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-09 22:07:36 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.009 |  |
| 2026-11-09 22:07:10 | Peradeniya (Mahaweli Ganga) | 5.05 | 🟡 Alert | 0.226 | 🔺 Rising |
| 2026-11-09 22:06:51 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-09 22:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 22:06:04 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-11-09 22:05:10 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-11-09 22:04:56 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-11-09 22:04:55 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 22:04:46 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:04:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-09 22:04:04 | Nawalapitiya (Mahaweli Ganga) | 3.21 | 🟢 Normal | -0.058 |  |
| 2026-11-09 22:04:00 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-09 22:03:43 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 22:03:36 | Rathnapura (Kalu Ganga) | 5.19 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-11-09 22:03:28 | Hanwella (Kelani Ganga) | 4.74 | 🟢 Normal | 0.567 | 🔺 Rising |
| 2026-11-09 22:03:03 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-09 22:03:03 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-09 22:02:55 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-11-09 22:02:48 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-09 22:02:26 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-11-09 22:02:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.394 |  |
| 2026-11-09 22:01:46 | Wellawaya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-11-09 22:01:41 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 22:01:17 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | 1.506 | 🔺 Rising |
| 2026-11-09 22:01:13 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.231 |  |
| 2026-11-09 22:01:12 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:00:44 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-11-09 22:00:38 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.135 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 22:03:03 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-09 22:01:17 | Moraketiya (Walawe Ganga) | 3.30 | 🟡 Alert | 1.506 | 🔺 Rising |
| 2026-11-09 22:07:10 | Peradeniya (Mahaweli Ganga) | 5.05 | 🟡 Alert | 0.226 | 🔺 Rising |
| 2026-11-09 22:00:38 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.135 | 🔺 Rising |
| 2026-11-09 22:08:46 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-11-09 22:06:04 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-11-09 22:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 22:04:55 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 21:13:54 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | -0.009 |  |
| 2026-11-09 22:02:55 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-11-09 22:02:26 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-11-09 22:03:28 | Hanwella (Kelani Ganga) | 4.74 | 🟢 Normal | 0.567 | 🔺 Rising |
| 2026-11-09 22:03:36 | Rathnapura (Kalu Ganga) | 5.19 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-11-09 22:04:56 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-11-09 22:02:48 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 22:06:51 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-09 22:07:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-09 22:01:41 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 22:03:43 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 22:04:00 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-09 22:15:05 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:01:12 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:04:46 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-09 22:07:36 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.009 |  |
| 2026-11-09 22:04:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-09 22:05:10 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-09 22:03:03 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-09 22:11:00 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.036 |  |
| 2026-11-09 22:00:44 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-11-09 22:04:04 | Nawalapitiya (Mahaweli Ganga) | 3.21 | 🟢 Normal | -0.058 |  |
| 2026-11-09 22:09:21 | Holombuwa (Kelani Ganga) | 1.84 | 🟢 Normal | -0.137 |  |
| 2026-11-09 22:01:46 | Wellawaya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-11-09 22:10:04 | Thaldena (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.200 |  |
| 2026-11-09 22:01:13 | Kithulgala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.231 |  |
| 2026-11-09 22:02:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.394 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)