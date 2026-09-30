# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_13:11:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 13:11:38 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.017 |  |
| 2026-09-30 13:10:49 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.009 |  |
| 2026-09-30 13:09:56 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-09-30 13:08:45 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:08:45 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-09-30 13:07:37 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:06:50 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:06:03 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:05:39 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:05:32 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.040 |  |
| 2026-09-30 13:05:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:05:12 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-09-30 13:04:56 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:04:17 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:04:07 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-30 13:04:04 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:03:49 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-09-30 13:03:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:03:24 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.031 |  |
| 2026-09-30 13:03:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-30 13:03:12 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.029 |  |
| 2026-09-30 13:02:49 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:41 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2026-09-30 13:02:36 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:34 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:27 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-30 13:02:27 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-30 13:02:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-30 13:02:15 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:01:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:00:59 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:00:57 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:00:45 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | -0.031 |  |
| 2026-09-30 13:00:09 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 12:57:34 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 13:02:27 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-30 13:02:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-30 13:02:18 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-30 13:04:07 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-30 13:03:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-30 13:02:49 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:01:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:03:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:06:50 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:00:59 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:04:56 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:41 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:00:09 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:05:39 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:05:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:06:03 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:04:17 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 12:00:41 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:07:37 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:02:34 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:08:45 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 13:10:49 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.009 |  |
| 2026-09-30 13:04:04 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:36 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:00:57 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:15 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:02:27 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.010 |  |
| 2026-09-30 13:11:38 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.017 |  |
| 2026-09-30 13:09:56 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-09-30 13:08:45 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-09-30 13:03:49 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-09-30 13:03:12 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.029 |  |
| 2026-09-30 13:05:12 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-09-30 13:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2026-09-30 13:00:45 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | -0.031 |  |
| 2026-09-30 13:03:24 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.031 |  |
| 2026-09-30 13:05:32 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.040 |  |
| 2026-09-30 12:57:34 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)