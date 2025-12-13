# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_07:20:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 07:20:28 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.048 |  |
| 2025-12-13 07:19:25 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.008 |  |
| 2025-12-13 07:08:56 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.036 |  |
| 2025-12-13 07:08:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:07:44 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.020 |  |
| 2025-12-13 07:07:36 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-13 07:07:34 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:07:34 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:07:11 | Weraganthota (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-13 07:06:55 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-13 07:06:37 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-13 07:06:22 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:05:24 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 07:05:20 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:05:19 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:04:38 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 07:04:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-13 07:04:25 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.102 |  |
| 2025-12-13 07:04:02 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:03:29 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-13 07:03:13 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-13 07:03:11 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 07:03:06 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-13 07:02:44 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:02:25 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.029 |  |
| 2025-12-13 07:02:09 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.084 |  |
| 2025-12-13 07:02:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-13 07:01:51 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.072 |  |
| 2025-12-13 07:01:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:01:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2025-12-13 07:01:39 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.023 |  |
| 2025-12-13 07:01:21 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2025-12-13 07:01:19 | Magura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2025-12-13 07:01:09 | Horowpothana (Yan Oya) | 6.11 | 🟡 Alert | -0.046 |  |
| 2025-12-13 07:01:08 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.076 |  |
| 2025-12-13 07:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 06:54:06 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-13 06:43:11 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 06:26:34 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 07:01:09 | Horowpothana (Yan Oya) | 6.11 | 🟡 Alert | -0.046 |  |
| 2025-12-13 06:00:22 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2025-12-13 07:06:37 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-13 07:07:36 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-13 07:07:11 | Weraganthota (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-13 07:03:13 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-13 07:04:38 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 07:05:24 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 07:03:29 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-13 07:02:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-13 07:03:11 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 07:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 07:01:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:02:44 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:04:02 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:05:20 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:08:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:07:34 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:05:19 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:06:22 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:07:34 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:02:25 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:19:25 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.008 |  |
| 2025-12-13 07:06:55 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-13 07:03:06 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:21:02 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.015 |  |
| 2025-12-13 07:07:44 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.020 |  |
| 2025-12-13 07:01:21 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2025-12-13 07:01:19 | Magura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2025-12-13 07:01:39 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.023 |  |
| 2025-12-13 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.029 |  |
| 2025-12-13 07:08:56 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.036 |  |
| 2025-12-13 07:01:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2025-12-13 07:20:28 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.048 |  |
| 2025-12-13 07:04:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-13 07:01:51 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.072 |  |
| 2025-12-13 07:01:08 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.076 |  |
| 2025-12-13 07:02:09 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.084 |  |
| 2025-12-13 07:04:25 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)