# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_11:10:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Nawalapitiya — Minor Flood; 🟡 Norwood — Alert; 🟡 Rathnapura — Alert; 🟡 Kithulgala — Alert; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 11:10:17 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:09:26 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:09:14 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:08:27 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.906 | 🔺 Rising |
| 2026-09-20 11:08:07 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-20 11:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-09-20 11:07:20 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-09-20 11:06:54 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-20 11:06:03 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | 0.293 | 🔺 Rising |
| 2026-09-20 11:05:46 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:05:37 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 11:05:27 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-09-20 11:05:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:05:18 | Pitabeddara (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-20 11:05:09 | Glencourse (Kelani Ganga) | 13.65 | 🟢 Normal | 0.981 | 🔺 Rising |
| 2026-09-20 11:04:57 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 11:04:38 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | 0.455 | 🔺 Rising |
| 2026-09-20 11:04:25 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 11:04:24 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-09-20 11:04:06 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-20 11:04:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:03:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:03:34 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | 0.744 | 🔺 Rising |
| 2026-09-20 11:03:12 | Deraniyagala (Kelani Ganga) | 4.28 | 🟢 Normal | 1.228 | 🔺 Rising |
| 2026-09-20 11:02:51 | Kithulgala (Kelani Ganga) | 3.15 | 🟡 Alert | 0.297 | 🔺 Rising |
| 2026-09-20 11:02:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:02:45 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-20 11:02:44 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:02:37 | Nawalapitiya (Mahaweli Ganga) | 5.70 | 🟠 Minor Flood | -0.349 |  |
| 2026-09-20 11:02:23 | Norwood (Kelani Ganga) | 2.68 | 🟡 Alert | 0.747 | 🔺 Rising |
| 2026-09-20 11:02:21 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-09-20 11:02:01 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-20 11:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:23 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:19 | Peradeniya (Mahaweli Ganga) | 4.95 | 🟢 Normal | 1.078 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 11:02:37 | Nawalapitiya (Mahaweli Ganga) | 5.70 | 🟠 Minor Flood | -0.349 |  |
| 2026-09-20 11:02:23 | Norwood (Kelani Ganga) | 2.68 | 🟡 Alert | 0.747 | 🔺 Rising |
| 2026-09-20 11:03:34 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | 0.744 | 🔺 Rising |
| 2026-09-20 11:02:51 | Kithulgala (Kelani Ganga) | 3.15 | 🟡 Alert | 0.297 | 🔺 Rising |
| 2026-09-20 11:06:03 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | 0.293 | 🔺 Rising |
| 2026-09-20 11:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-09-20 11:04:24 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-09-20 11:03:12 | Deraniyagala (Kelani Ganga) | 4.28 | 🟢 Normal | 1.228 | 🔺 Rising |
| 2026-09-20 11:01:19 | Peradeniya (Mahaweli Ganga) | 4.95 | 🟢 Normal | 1.078 | 🔺 Rising |
| 2026-09-20 11:05:09 | Glencourse (Kelani Ganga) | 13.65 | 🟢 Normal | 0.981 | 🔺 Rising |
| 2026-09-20 11:08:27 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.906 | 🔺 Rising |
| 2026-09-20 11:04:38 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | 0.455 | 🔺 Rising |
| 2026-09-20 11:07:20 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-09-20 11:05:27 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-09-20 11:05:18 | Pitabeddara (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-20 11:04:06 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-20 11:08:07 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-20 11:06:54 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-20 11:02:45 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-20 11:04:57 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 11:05:37 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 11:04:25 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 10:00:43 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 11:09:26 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:02:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:10:17 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:09:14 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:05:46 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:03:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:05:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:02:44 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:04:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:01:23 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:02:01 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-20 11:02:21 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)