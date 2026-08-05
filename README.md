# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_18:16:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,800 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 18:16:26 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:08:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:07:36 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | -0.085 |  |
| 2026-08-05 18:05:38 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-08-05 18:05:35 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:05:13 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.123 |  |
| 2026-08-05 18:04:58 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.077 |  |
| 2026-08-05 18:04:54 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 18:04:51 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:04:49 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:04:42 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.115 |  |
| 2026-08-05 18:04:36 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-05 18:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:03:59 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-08-05 18:03:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-05 18:03:52 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-08-05 18:03:39 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.050 |  |
| 2026-08-05 18:03:37 | Deraniyagala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-08-05 18:03:27 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:03:24 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-08-05 18:03:10 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-08-05 18:03:00 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2026-08-05 18:02:46 | Peradeniya (Mahaweli Ganga) | 6.39 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-08-05 18:02:33 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-05 18:02:23 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:02:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.040 |  |
| 2026-08-05 18:02:06 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-05 18:01:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-05 18:01:39 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.011 |  |
| 2026-08-05 18:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:00 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-08-05 18:00:46 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:00:09 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 18:02:46 | Peradeniya (Mahaweli Ganga) | 6.39 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-08-05 18:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-05 18:01:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-05 18:04:54 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 18:02:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:08:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:04:49 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:00:46 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:04:51 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:16:26 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:02:23 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:05:35 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:00:09 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:02:06 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-05 18:01:39 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.011 |  |
| 2026-08-05 18:02:33 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-05 18:05:38 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-08-05 18:04:36 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-05 18:03:52 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-08-05 18:03:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-05 18:03:10 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-08-05 18:03:37 | Deraniyagala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-08-05 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.040 |  |
| 2026-08-05 18:03:00 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2026-08-05 18:03:24 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-08-05 18:03:59 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-08-05 18:03:39 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.050 |  |
| 2026-08-05 18:01:00 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-08-05 18:04:58 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.077 |  |
| 2026-08-05 18:07:36 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | -0.085 |  |
| 2026-08-05 18:04:42 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.115 |  |
| 2026-08-05 18:05:13 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)