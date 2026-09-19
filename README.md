# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_00:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 00:18:16 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-20 00:16:49 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:16:15 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.049 |  |
| 2026-09-20 00:13:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 00:09:11 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:09:06 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:08:45 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-20 00:07:40 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-09-20 00:06:26 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:06:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-09-20 00:05:50 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-20 00:05:10 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:51 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -360.000 |  |
| 2026-09-20 00:04:50 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -360.000 |  |
| 2026-09-20 00:04:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:04:39 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:33 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.111 |  |
| 2026-09-20 00:04:18 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-20 00:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:14 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:04:09 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.041 |  |
| 2026-09-20 00:03:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:02:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:40 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:34 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 00:02:17 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:13 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:12 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-20 00:02:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-20 00:01:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:43 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:41 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:09 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.091 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 00:04:18 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-20 00:01:09 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-20 00:05:50 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-20 00:02:12 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-20 00:13:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 00:08:45 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-20 00:02:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 00:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 23:00:54 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 00:18:16 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-20 00:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:43 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:34 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:33 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:01:41 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:05:10 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:13 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:09:06 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:06:26 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:17 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:02:40 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:04:39 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 00:16:49 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:09:11 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:03:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:04:14 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:04:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-20 00:06:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-09-20 00:07:40 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-09-20 00:04:09 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.041 |  |
| 2026-09-20 00:16:15 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.049 |  |
| 2026-09-20 00:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.111 |  |
| 2026-09-20 00:04:51 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -360.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)