# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_18:13:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 18:13:46 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:11:25 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:09:54 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:07:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-31 18:06:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-31 18:06:06 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:06:02 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:05:28 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | 0.610 | 🔺 Rising |
| 2025-12-31 18:05:01 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:05:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.022 |  |
| 2025-12-31 18:04:50 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:04:34 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:47 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:03:42 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.028 |  |
| 2025-12-31 18:03:14 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-31 18:02:56 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2025-12-31 18:02:49 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2025-12-31 18:02:09 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2025-12-31 18:02:04 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:02:01 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:44 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-31 18:01:35 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2025-12-31 18:01:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-31 18:01:11 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:01:03 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:00:46 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2025-12-31 18:00:23 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:00:11 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:52:50 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:22:28 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 18:05:28 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | 0.610 | 🔺 Rising |
| 2025-12-31 18:02:56 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2025-12-31 18:01:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-31 18:06:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-31 18:03:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-31 18:07:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-31 18:01:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 18:01:44 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 17:06:48 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 17:06:17 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 18:02:01 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:14 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:13:46 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:04:34 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:02:04 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:11:25 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:03 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:02:49 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:06:06 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:05:01 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:06:02 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:09:54 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:42 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:00:11 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:03:47 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:04:50 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:01:11 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-31 18:01:35 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2025-12-31 18:05:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.022 |  |
| 2025-12-31 18:03:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.028 |  |
| 2025-12-31 18:00:46 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2025-12-31 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2025-12-31 18:00:23 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2025-12-31 18:02:09 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)