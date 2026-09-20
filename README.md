# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_08:10:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,870 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Nawalapitiya — Major Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 08:10:00 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 08:09:12 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 1.092 | 🔺 Rising |
| 2026-09-20 08:08:56 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-09-20 08:08:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:08:34 | Thawalama (Gin Ganga) | 3.59 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 08:07:50 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-20 08:07:28 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-20 08:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-20 08:06:25 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-20 08:06:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:05:56 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:05:01 | Magura (Kalu Ganga) | 4.54 | 🟡 Alert | 0.164 | 🔺 Rising |
| 2026-09-20 08:04:41 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | -0.059 |  |
| 2026-09-20 08:04:35 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:04:31 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:04:29 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.923 | 🔺 Rising |
| 2026-09-20 08:04:26 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-09-20 08:04:19 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-09-20 08:03:50 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:03:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-09-20 08:03:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:03:34 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-09-20 08:02:51 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:02:36 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 08:02:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:02:21 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:02:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:02:06 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:01:55 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:51 | Nawalapitiya (Mahaweli Ganga) | 6.00 | 🔴 Major Flood | 1.339 | 🔺 Rising |
| 2026-09-20 08:01:46 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:44 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-20 08:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:13 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:00:54 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:00:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:25:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.160 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 08:01:51 | Nawalapitiya (Mahaweli Ganga) | 6.00 | 🔴 Major Flood | 1.339 | 🔺 Rising |
| 2026-09-20 08:05:01 | Magura (Kalu Ganga) | 4.54 | 🟡 Alert | 0.164 | 🔺 Rising |
| 2026-09-20 08:09:12 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 1.092 | 🔺 Rising |
| 2026-09-20 08:04:29 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.923 | 🔺 Rising |
| 2026-09-20 08:04:19 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-09-20 08:08:34 | Thawalama (Gin Ganga) | 3.59 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-09-20 08:08:56 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-09-20 08:04:26 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-09-20 08:03:34 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-09-20 08:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-20 08:10:00 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 07:08:38 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-20 08:06:25 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-20 08:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-20 08:01:44 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-20 08:07:50 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-20 08:02:36 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 08:04:31 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:02:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:07:28 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:01:13 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 08:02:21 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:55 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:00:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:03:50 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:04:35 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:06:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:08:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:05:56 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:03:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:01:46 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:02:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 08:00:54 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:02:51 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:02:06 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-20 08:03:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-09-20 08:04:41 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)