# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_04:30:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Nawalapitiya — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 04:30:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:26:49 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.037 |  |
| 2026-08-05 04:15:33 | Nawalapitiya (Mahaweli Ganga) | 3.71 | 🟡 Alert | 0.277 | 🔺 Rising |
| 2026-08-05 04:13:59 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.035 |  |
| 2026-08-05 04:10:52 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:10:48 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.036 |  |
| 2026-08-05 04:09:34 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.018 |  |
| 2026-08-05 04:07:42 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-08-05 04:06:00 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:04:56 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:04:37 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.110 |  |
| 2026-08-05 04:04:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 04:04:05 | Peradeniya (Mahaweli Ganga) | 4.51 | 🟢 Normal | -0.019 |  |
| 2026-08-05 04:03:48 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:46 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:03:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:35 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:09 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:03:09 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.038 |  |
| 2026-08-05 04:02:35 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:02:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:12 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-05 04:02:05 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:01:50 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-08-05 04:01:49 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:01:20 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:00:37 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:50:23 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 04:15:33 | Nawalapitiya (Mahaweli Ganga) | 3.71 | 🟡 Alert | 0.277 | 🔺 Rising |
| 2026-08-05 03:13:21 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.132 |  |
| 2026-08-05 04:02:12 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-05 04:04:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 04:00:37 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:17:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:01:49 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:48 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:04:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:35 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:07:09 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:19:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:30:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:05 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:03:35 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:01:20 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:02:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:03:09 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:04:56 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 04:01:50 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-08-05 03:04:46 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-08-05 04:09:34 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.018 |  |
| 2026-08-05 04:04:05 | Peradeniya (Mahaweli Ganga) | 4.51 | 🟢 Normal | -0.019 |  |
| 2026-08-05 04:03:46 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:06:00 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:10:52 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:07:42 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-08-05 04:13:59 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.035 |  |
| 2026-08-05 04:10:48 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.036 |  |
| 2026-08-05 04:26:49 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.037 |  |
| 2026-08-05 04:03:09 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.038 |  |
| 2026-08-05 03:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.053 |  |
| 2026-08-05 04:04:37 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.110 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-05 03:13:02 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)