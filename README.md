# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_17:20:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,449 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 17:20:20 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | -0.016 |  |
| 2026-10-18 17:14:28 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-18 17:12:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-10-18 17:12:01 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-10-18 17:09:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.071 |  |
| 2026-10-18 17:09:40 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-18 17:08:07 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:07:25 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-10-18 17:06:33 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.058 |  |
| 2026-10-18 17:06:27 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:05:38 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-10-18 17:05:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-18 17:05:10 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:04:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.059 |  |
| 2026-10-18 17:04:52 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-10-18 17:03:52 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-10-18 17:03:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:03:28 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:03:22 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.081 |  |
| 2026-10-18 17:03:17 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-18 17:03:03 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-10-18 17:03:02 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.040 |  |
| 2026-10-18 17:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-18 17:02:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:02:27 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-18 17:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:53 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 17:01:44 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:41 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:36 | Pitabeddara (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-18 17:01:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:06 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.129 |  |
| 2026-10-18 17:01:05 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.091 |  |
| 2026-10-18 17:00:39 | Moragaswewa (Deduru Oya) | 2.57 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-18 17:00:31 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.089 |  |
| 2026-10-18 17:00:16 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-18 17:00:15 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 17:00:11 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.092 |  |
| 2026-10-18 16:59:50 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.096 |  |
| 2026-10-18 16:51:50 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.129 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 17:00:15 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 17:07:25 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-10-18 17:20:20 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | -0.016 |  |
| 2026-10-18 17:03:52 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-10-18 17:01:36 | Pitabeddara (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-18 17:00:39 | Moragaswewa (Deduru Oya) | 2.57 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-18 17:09:40 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-18 17:05:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-18 17:14:28 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-18 17:00:16 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-18 17:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-18 17:01:53 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 17:05:10 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:03:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:02:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:44 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:06:27 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:03:28 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:08:07 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:01:41 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 17:03:17 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-18 17:02:27 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-18 17:12:01 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-10-18 17:03:03 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-10-18 17:05:38 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-10-18 17:12:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-10-18 17:04:52 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-10-18 17:03:02 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.040 |  |
| 2026-10-18 17:06:33 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.058 |  |
| 2026-10-18 17:04:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.059 |  |
| 2026-10-18 17:09:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.071 |  |
| 2026-10-18 17:03:22 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.081 |  |
| 2026-10-18 17:00:31 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.089 |  |
| 2026-10-18 17:01:05 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.091 |  |
| 2026-10-18 17:00:11 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.092 |  |
| 2026-10-18 16:59:50 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.096 |  |
| 2026-10-18 17:01:06 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)