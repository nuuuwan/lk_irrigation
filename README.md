# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_02:34:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 02:34:58 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.013 |  |
| 2026-01-13 02:31:36 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-01-13 02:26:54 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.137 |  |
| 2026-01-13 02:22:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:22:33 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:14:55 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-13 02:11:50 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.080 |  |
| 2026-01-13 02:08:43 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:08:41 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:08:40 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 02:06:29 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:06:17 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 02:06:01 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.468 |  |
| 2026-01-13 02:04:24 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-13 02:03:59 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-01-13 02:03:57 | Horowpothana (Yan Oya) | 3.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 02:03:55 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:31 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.468 |  |
| 2026-01-13 02:03:24 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 02:02:45 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.027 |  |
| 2026-01-13 02:01:59 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:01:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 02:01:17 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-13 02:01:13 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:01:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 02:00:58 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 00:13:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-13 02:14:55 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-13 02:03:10 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 01:04:55 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 01:00:36 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 02:03:57 | Horowpothana (Yan Oya) | 3.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 02:01:31 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 02:06:17 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 02:01:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 00:02:24 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 02:08:40 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:55 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:01:13 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 00:11:33 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:00:58 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:08:43 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:17 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:01:59 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:06:29 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:22:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:06:01 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:24 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 01:07:44 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:59 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-01-13 01:03:42 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:01:47 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 02:04:24 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-13 02:34:58 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.013 |  |
| 2026-01-13 02:01:17 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-13 02:31:36 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-01-13 02:02:45 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.027 |  |
| 2026-01-13 01:01:13 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-01-13 02:11:50 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.080 |  |
| 2026-01-13 02:26:54 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.137 |  |
| 2026-01-13 02:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.468 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)