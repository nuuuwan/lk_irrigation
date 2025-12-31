# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_19:11:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 19:11:23 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:11:13 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:10:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.027 |  |
| 2025-12-31 19:09:28 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:08:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:07:59 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:07:20 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:06:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2025-12-31 19:06:27 | Nakkala (Kumbukkan Oya) | 3.96 | 🟢 Normal | 2.418 | 🔺 Rising |
| 2025-12-31 19:06:15 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-31 19:05:34 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:04:55 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:04:34 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-31 19:04:18 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-31 19:04:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:04:02 | Siyambalanduwa (Heda Oya) | 2.15 | 🟢 Normal | 1.429 | 🔺 Rising |
| 2025-12-31 19:03:57 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:03:53 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 19:03:41 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 19:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 19:03:35 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2025-12-31 19:03:07 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:02:43 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-31 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-31 19:02:11 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-31 19:01:56 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:01:54 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 19:01:35 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2025-12-31 19:01:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 19:01:24 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:01:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-31 19:01:02 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 19:06:27 | Nakkala (Kumbukkan Oya) | 3.96 | 🟢 Normal | 2.418 | 🔺 Rising |
| 2025-12-31 19:04:02 | Siyambalanduwa (Heda Oya) | 2.15 | 🟢 Normal | 1.429 | 🔺 Rising |
| 2025-12-31 19:03:35 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2025-12-31 19:04:18 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-31 19:01:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-31 19:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 19:02:11 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-31 19:04:34 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-31 19:01:35 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 19:03:53 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 19:03:41 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 19:01:54 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 19:06:15 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-31 19:01:24 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:04:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:11:13 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:07:59 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:04:34 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:05:34 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:03:07 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:08:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:01:56 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:04:55 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:03 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:03:57 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:09:28 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:07:20 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:11:23 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:01:02 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:06:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2025-12-31 19:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-31 19:01:35 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2025-12-31 19:02:43 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-31 19:10:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.027 |  |
| 2025-12-31 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)