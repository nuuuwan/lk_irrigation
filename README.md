# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_03:26:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 03:26:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:21:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:08:59 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-21 03:08:08 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-01-21 03:07:07 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 5.569 | 🔺 Rising |
| 2026-01-21 03:06:40 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:06:30 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:06:19 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 03:06:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-21 03:05:10 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 03:05:10 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:05:03 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:04:22 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:04:00 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-21 03:03:58 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:03:26 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-01-21 03:03:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -1.500 |  |
| 2026-01-21 03:03:04 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:03:00 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -1.500 |  |
| 2026-01-21 03:02:50 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-21 03:02:34 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:02:02 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.149 |  |
| 2026-01-21 03:01:59 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:58 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.003 |  |
| 2026-01-21 03:01:47 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 03:01:35 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-01-21 03:01:16 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:00:52 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 02:59:28 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 5.569 | 🔺 Rising |
| 2026-01-21 02:54:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.831 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 03:07:07 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 5.569 | 🔺 Rising |
| 2026-01-21 03:01:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-01-21 03:06:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-21 03:04:00 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-21 03:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-21 03:08:59 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-21 03:06:19 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 02:05:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 03:05:10 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 03:01:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 03:01:16 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:59 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:00:52 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 02:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:04 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:03:58 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:21:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:06:30 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:26:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:04:22 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:47 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:02:34 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:05:10 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:12:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:06:40 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:05:03 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:01:58 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.003 |  |
| 2026-01-21 03:08:08 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-01-21 03:03:04 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:01:35 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:02:50 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-21 03:03:26 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-01-21 03:02:02 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.149 |  |
| 2026-01-21 03:03:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)