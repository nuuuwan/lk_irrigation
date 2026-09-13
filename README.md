# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_20:16:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,050 measurements** from **39** stations.
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
| 2026-09-13 20:16:45 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-09-13 20:13:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:12:37 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.026 |  |
| 2026-09-13 20:09:46 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-09-13 20:09:33 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:09:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-09-13 20:08:11 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.011 |  |
| 2026-09-13 20:06:55 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:47 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-09-13 20:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:05 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 20:04:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-13 20:04:53 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-13 20:04:31 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.084 |  |
| 2026-09-13 20:03:57 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 1.917 | 🔺 Rising |
| 2026-09-13 20:03:45 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-09-13 20:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 20:03:02 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.093 |  |
| 2026-09-13 20:02:44 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-09-13 20:02:38 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:32 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:17 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-09-13 20:02:15 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:13 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 20:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:09 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-13 20:01:44 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.121 |  |
| 2026-09-13 20:01:37 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:33 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:26 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:00:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:00:07 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 20:03:57 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 1.917 | 🔺 Rising |
| 2026-09-13 20:02:44 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-09-13 20:04:53 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-13 20:02:09 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-13 20:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 20:06:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 20:02:13 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:32 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:00:07 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:03:02 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:15 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:44 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:38 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:55 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:09:33 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:33 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:00:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:02:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:05 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:37 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:13:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:01:26 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:09:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-09-13 20:04:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-13 20:08:11 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.011 |  |
| 2026-09-13 20:16:45 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-09-13 20:03:45 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-09-13 20:12:37 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.026 |  |
| 2026-09-13 20:09:46 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-09-13 20:02:17 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-09-13 20:04:31 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.084 |  |
| 2026-09-13 20:02:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.093 |  |
| 2026-09-13 20:06:47 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-09-13 20:01:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)