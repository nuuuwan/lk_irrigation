# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_02:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 02:13:33 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.095 |  |
| 2026-08-05 02:13:16 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-08-05 02:09:52 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-08-05 02:08:54 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-08-05 02:07:50 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-08-05 02:05:24 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:05:14 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-05 02:05:06 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:04:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-08-05 02:04:23 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-05 02:04:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:03:54 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-08-05 02:03:35 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:03:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 02:03:06 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | -0.081 |  |
| 2026-08-05 02:02:54 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:02:07 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-05 02:01:58 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:47 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-05 02:01:22 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:00:35 | Rathnapura (Kalu Ganga) | 5.51 | 🟡 Alert | -0.093 |  |
| 2026-08-05 01:46:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:40:48 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 00:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.059 |  |
| 2026-08-05 02:00:35 | Rathnapura (Kalu Ganga) | 5.51 | 🟡 Alert | -0.093 |  |
| 2026-08-05 01:02:46 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-08-05 02:05:14 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-05 02:04:23 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-05 02:03:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 02:01:47 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-05 02:04:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:01:20 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:03:35 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:58 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:02:06 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:46:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:02:54 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:05:06 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:05:01 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:05:24 | Peradeniya (Mahaweli Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:22 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:08:54 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-08-05 00:04:00 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-08-05 02:04:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-08-05 01:05:14 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 02:03:54 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-08-05 01:05:03 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-05 02:02:07 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-05 00:02:44 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-08-05 02:07:50 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-08-05 01:03:51 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-08-05 01:06:55 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.038 |  |
| 2026-08-05 02:13:16 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-08-05 01:40:48 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.042 |  |
| 2026-08-05 02:09:52 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-08-05 02:03:06 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | -0.081 |  |
| 2026-08-05 02:13:33 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.095 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)