# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_20:31:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 20:31:12 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.014 |  |
| 2026-08-04 20:16:36 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 20:13:24 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-08-04 20:10:41 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.071 |  |
| 2026-08-04 20:09:54 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 20:08:51 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.156 |  |
| 2026-08-04 20:08:39 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.061 |  |
| 2026-08-04 20:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-08-04 20:07:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 20:07:33 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-04 20:07:09 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-04 20:06:27 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-08-04 20:06:12 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.057 |  |
| 2026-08-04 20:06:03 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-08-04 20:05:56 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.029 |  |
| 2026-08-04 20:05:46 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-08-04 20:05:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:05:21 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:05:04 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:04:01 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | -0.286 |  |
| 2026-08-04 20:03:44 | Rathnapura (Kalu Ganga) | 6.04 | 🟡 Alert | -0.010 |  |
| 2026-08-04 20:03:43 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-08-04 20:03:37 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-04 20:03:03 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-08-04 20:02:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:15 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | -0.121 |  |
| 2026-08-04 20:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:03 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-08-04 20:01:52 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:01:45 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:01:07 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-04 20:01:05 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 20:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-08-04 20:03:44 | Rathnapura (Kalu Ganga) | 6.04 | 🟡 Alert | -0.010 |  |
| 2026-08-04 20:03:37 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-04 20:16:36 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 20:07:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 20:09:54 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 20:07:33 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-04 20:01:45 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:03 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:05:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:05:21 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:05:04 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:01:52 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:01:05 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 20:13:24 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-08-04 20:07:09 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-04 20:06:27 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-08-04 20:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-08-04 20:31:12 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.014 |  |
| 2026-08-04 20:03:03 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-08-04 20:05:46 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-08-04 20:01:07 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-04 20:03:43 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-08-04 20:05:56 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.029 |  |
| 2026-08-04 18:11:17 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.038 |  |
| 2026-08-04 20:06:03 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-08-04 20:06:12 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.057 |  |
| 2026-08-04 20:08:39 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.061 |  |
| 2026-08-04 20:10:41 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.071 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 20:02:15 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | -0.121 |  |
| 2026-08-04 20:08:51 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.156 |  |
| 2026-08-04 20:04:01 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | -0.286 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)