# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_19:19:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,310 measurements** from **39** stations.
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
| 2026-09-30 19:19:27 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-09-30 19:12:49 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-09-30 19:10:14 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.041 |  |
| 2026-09-30 19:08:31 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.027 |  |
| 2026-09-30 19:07:59 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-09-30 19:07:51 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-09-30 19:07:42 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:06:03 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-09-30 19:06:01 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:05:58 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:05:46 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-30 19:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-09-30 19:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:05:00 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-30 19:04:39 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:04:31 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 19:03:57 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-09-30 19:03:36 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:03:33 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:03:24 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.042 |  |
| 2026-09-30 19:03:16 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-09-30 19:03:08 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 19:02:59 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:58 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:02:56 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |
| 2026-09-30 19:02:40 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-09-30 19:02:25 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-09-30 19:02:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:11 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.049 |  |
| 2026-09-30 19:01:47 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:01:11 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-30 19:00:46 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:00:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 19:03:57 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-09-30 19:02:40 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 19:01:11 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-30 19:05:46 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-30 19:05:00 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-30 19:04:31 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 19:02:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 19:02:59 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:56 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:00:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:04:39 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:06:01 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:02:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:07:42 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:03:08 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 19:19:27 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-09-30 19:07:59 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-09-30 19:07:51 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-09-30 19:05:58 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:03:33 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:00:46 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:02:58 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:03:36 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:01:47 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.010 |  |
| 2026-09-30 19:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-09-30 19:02:25 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-09-30 19:12:49 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-09-30 19:08:31 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.027 |  |
| 2026-09-30 19:06:03 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-09-30 19:03:16 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-09-30 19:10:14 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.041 |  |
| 2026-09-30 19:03:24 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.042 |  |
| 2026-09-30 19:02:11 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.049 |  |
| 2026-09-30 19:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)