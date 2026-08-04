# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_22:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 22:14:32 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:11:22 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.044 |  |
| 2026-08-04 22:11:20 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-08-04 22:09:43 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.027 |  |
| 2026-08-04 22:09:21 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 22:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.031 |  |
| 2026-08-04 22:07:57 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:07:42 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:06:27 | Kithulgala (Kelani Ganga) | 3.02 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-08-04 22:05:26 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.039 |  |
| 2026-08-04 22:05:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-08-04 22:05:00 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-08-04 22:04:48 | Deraniyagala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.314 |  |
| 2026-08-04 22:04:32 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:04:25 | Glencourse (Kelani Ganga) | 13.28 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-04 22:03:54 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-08-04 22:03:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:03:46 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:03:24 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:03:11 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:02:54 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:02:32 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | -0.020 |  |
| 2026-08-04 22:02:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-04 22:02:20 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-04 22:02:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:40 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:38 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:10 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:04 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:00:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:00:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:00:53 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:00:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:59:58 | Rathnapura (Kalu Ganga) | 5.90 | 🟡 Alert | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 22:06:27 | Kithulgala (Kelani Ganga) | 3.02 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-08-04 22:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.031 |  |
| 2026-08-04 21:59:58 | Rathnapura (Kalu Ganga) | 5.90 | 🟡 Alert | -0.091 |  |
| 2026-08-04 22:04:25 | Glencourse (Kelani Ganga) | 13.28 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-04 22:02:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-04 22:09:21 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 22:00:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:04 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:00:53 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:02:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:38 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:03:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:07:42 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:03:24 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:04:32 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:14:32 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:10 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:40 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:00:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:03:46 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:07:57 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-04 22:05:00 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-08-04 22:11:20 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-08-04 22:05:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-08-04 22:02:32 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | -0.020 |  |
| 2026-08-04 22:02:20 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-04 22:00:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:02:54 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:03:11 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-08-04 21:02:27 | Peradeniya (Mahaweli Ganga) | 4.66 | 🟢 Normal | -0.021 |  |
| 2026-08-04 22:09:43 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.027 |  |
| 2026-08-04 22:05:26 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.039 |  |
| 2026-08-04 22:11:22 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.044 |  |
| 2026-08-04 22:03:54 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 22:04:48 | Deraniyagala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.314 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)