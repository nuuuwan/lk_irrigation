# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_07:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 07:16:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-01-03 07:11:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-01-03 07:10:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-03 07:10:05 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:09:43 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:08:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-03 07:08:13 | Galgamuwa (Mee Oya) | 1.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 07:07:32 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.038 |  |
| 2026-01-03 07:06:58 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-03 07:06:45 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:41 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:05:12 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:56 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:04:20 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-01-03 07:04:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:03 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.028 |  |
| 2026-01-03 07:04:01 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.290 |  |
| 2026-01-03 07:03:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-03 07:03:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:03:37 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:03:36 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.137 |  |
| 2026-01-03 07:03:00 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-01-03 07:02:58 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:38 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:36 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:30 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:01:39 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:01:33 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.044 |  |
| 2026-01-03 07:01:30 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:01:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.008 |  |
| 2026-01-03 07:00:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:59:50 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.031 |  |
| 2026-01-03 06:33:29 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 07:10:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-03 07:08:13 | Galgamuwa (Mee Oya) | 1.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 07:03:36 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:09:43 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:30 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:58 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:01:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:00:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:58 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:36 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:45 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:10:05 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:01:39 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:38 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:10:20 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:03:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:04:56 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:41 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:04:27 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.008 |  |
| 2026-01-03 07:05:12 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:03:37 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:01:30 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:16:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-01-03 07:03:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-03 06:02:49 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-01-03 07:11:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-01-03 07:04:03 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.028 |  |
| 2026-01-03 07:03:00 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-01-03 06:59:50 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.031 |  |
| 2026-01-03 07:07:32 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.038 |  |
| 2026-01-03 07:04:20 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-01-03 07:01:33 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.044 |  |
| 2026-01-03 07:08:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-03 07:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-03 07:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.137 |  |
| 2026-01-03 07:04:01 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.290 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)