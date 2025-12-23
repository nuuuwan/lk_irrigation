# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_06:11:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,454 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 06:08:53 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:07:25 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-23 06:07:24 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-23 06:06:12 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-23 06:05:14 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.019 |  |
| 2025-12-23 06:05:13 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 06:04:51 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:49 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:07 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:04 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.024 |  |
| 2025-12-23 06:04:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:03:47 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-23 06:03:39 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 06:03:18 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:02:47 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:02:34 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-23 06:02:27 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-23 06:02:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-23 06:02:23 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:02:14 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.049 |  |
| 2025-12-23 06:01:55 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.100 |  |
| 2025-12-23 06:01:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:01:39 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:01:28 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 06:01:26 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.093 |  |
| 2025-12-23 06:00:40 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.031 |  |
| 2025-12-23 06:00:24 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2025-12-23 06:00:11 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:55:50 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:32:50 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:31:12 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:14:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.100 |  |
| 2025-12-23 05:13:48 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 06:07:25 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2025-12-23 05:02:37 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2025-12-23 06:02:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-23 06:06:12 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-23 06:02:27 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-23 06:05:13 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 06:03:39 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 06:01:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:01:39 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:08:53 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 05:32:50 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:00:11 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:03:18 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:49 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:51 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:04:07 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:02:23 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:02:47 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 06:03:47 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-23 06:01:28 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 06:02:34 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-23 05:11:53 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.016 |  |
| 2025-12-23 06:05:14 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.019 |  |
| 2025-12-23 06:00:24 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2025-12-23 06:04:04 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.024 |  |
| 2025-12-23 05:03:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-23 06:00:40 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.031 |  |
| 2025-12-23 05:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.044 |  |
| 2025-12-23 06:02:14 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.049 |  |
| 2025-12-23 05:04:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.065 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-23 06:01:26 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.093 |  |
| 2025-12-23 06:01:55 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.100 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)