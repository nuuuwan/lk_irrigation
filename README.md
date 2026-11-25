# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_05:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 05:14:58 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-25 05:14:56 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-25 05:14:12 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:13:54 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:12:36 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.057 |  |
| 2026-11-25 05:11:53 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-25 05:11:07 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.046 |  |
| 2026-11-25 05:10:20 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-25 05:09:04 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:08:49 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.029 |  |
| 2026-11-25 05:08:14 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 05:06:43 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | -0.038 |  |
| 2026-11-25 05:06:32 | Urawa (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-11-25 05:06:25 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.118 |  |
| 2026-11-25 05:04:07 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | -0.135 |  |
| 2026-11-25 05:04:00 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:03:54 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.137 |  |
| 2026-11-25 05:03:45 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.137 |  |
| 2026-11-25 05:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-11-25 05:03:39 | Hanwella (Kelani Ganga) | 4.04 | 🟢 Normal | -0.040 |  |
| 2026-11-25 05:03:33 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 05:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-11-25 05:02:54 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-11-25 05:02:52 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-11-25 05:02:48 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:02:35 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.222 |  |
| 2026-11-25 05:02:15 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:02:00 | Moraketiya (Walawe Ganga) | 3.40 | 🟡 Alert | -0.097 |  |
| 2026-11-25 05:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:00:54 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:00:47 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:00:07 | Siyambalanduwa (Heda Oya) | 2.05 | 🟢 Normal | -0.092 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 05:06:43 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | -0.038 |  |
| 2026-11-25 05:02:00 | Moraketiya (Walawe Ganga) | 3.40 | 🟡 Alert | -0.097 |  |
| 2026-11-25 05:14:58 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-25 05:02:52 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-11-25 05:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-11-25 05:03:33 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 04:36:39 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-25 04:06:17 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-25 03:02:44 | Kuda Oya (Kirindi Oya) | 2.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 05:08:14 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 05:11:53 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-25 05:10:20 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-25 04:39:30 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-11-25 05:00:47 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-25 04:36:18 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:02:48 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:09:04 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:14:12 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 05:04:00 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:00:54 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:02:15 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:02:54 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-25 05:06:32 | Urawa (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 05:08:49 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.029 |  |
| 2026-11-25 05:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-11-25 05:03:39 | Hanwella (Kelani Ganga) | 4.04 | 🟢 Normal | -0.040 |  |
| 2026-11-25 05:11:07 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.046 |  |
| 2026-11-25 05:12:36 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.057 |  |
| 2026-11-25 05:00:07 | Siyambalanduwa (Heda Oya) | 2.05 | 🟢 Normal | -0.092 |  |
| 2026-11-25 05:06:25 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.118 |  |
| 2026-11-25 05:04:07 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | -0.135 |  |
| 2026-11-25 05:03:54 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.137 |  |
| 2026-11-25 05:03:45 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.137 |  |
| 2026-11-25 05:02:35 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)