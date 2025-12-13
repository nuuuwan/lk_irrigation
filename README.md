# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_22:07:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 22:07:02 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 22:06:31 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:05:46 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2025-12-13 22:05:33 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:04:24 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:04:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 22:04:05 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2025-12-13 22:04:01 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:46 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:41 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-13 22:03:27 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:21 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:03:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:11 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:03:01 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:02:46 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:02:36 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-13 22:02:29 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 22:02:26 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-13 22:02:17 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:02:15 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.061 |  |
| 2025-12-13 22:02:12 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 22:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:53 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-13 22:01:44 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:37 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:30 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:00:44 | Horowpothana (Yan Oya) | 5.39 | 🟢 Normal | -0.052 |  |
| 2025-12-13 21:36:07 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.007 |  |
| 2025-12-13 21:14:26 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:09:28 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.064 |  |
| 2025-12-13 21:08:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 21:06:09 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-13 22:02:26 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-13 22:01:53 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-13 22:07:02 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 21:02:07 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 22:02:12 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 22:04:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 22:02:29 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 22:03:41 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-13 22:03:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:44 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:04:24 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:01 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:06:31 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:27 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:04:01 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:07:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:01:37 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 22:03:46 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:36:07 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.007 |  |
| 2025-12-13 22:05:33 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:02:17 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:03:21 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:01:30 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:02:13 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:03:11 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:02:36 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-13 22:04:05 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2025-12-13 21:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.029 |  |
| 2025-12-13 22:05:46 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 22:00:44 | Horowpothana (Yan Oya) | 5.39 | 🟢 Normal | -0.052 |  |
| 2025-12-13 22:02:15 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.061 |  |
| 2025-12-13 21:09:28 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)