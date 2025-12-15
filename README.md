# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_12:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 12:14:20 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 12:13:52 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:11:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 12:10:39 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:07:56 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:07:45 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.021 |  |
| 2025-12-15 12:06:08 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:06:04 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:05:55 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:05:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2025-12-15 12:05:36 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:05:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:04:20 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-15 12:04:00 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:04:00 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.040 |  |
| 2025-12-15 12:03:56 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:03:49 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 12:03:47 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2025-12-15 12:03:23 | Horowpothana (Yan Oya) | 3.97 | 🟢 Normal | -0.038 |  |
| 2025-12-15 12:03:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:03:00 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | -0.024 |  |
| 2025-12-15 12:02:54 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:53 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:37 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:27 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:02:20 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:56 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2025-12-15 12:01:46 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:01:34 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:28 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 12:01:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:21 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:19 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-15 12:01:18 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 12:00:43 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 12:14:20 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 12:03:49 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 12:01:18 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 12:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 12:11:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 12:02:37 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:21 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:07:56 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:06:13 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:34 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:05:36 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:13:52 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:54 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:03:56 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:05:43 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:06:04 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:10:39 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:20 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:02:53 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:01:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 12:06:08 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:05:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:03:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:04:00 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:01:46 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:05:55 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:02:27 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:01:28 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-15 12:04:20 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-15 12:00:43 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-15 12:01:19 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-15 12:03:47 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2025-12-15 12:07:45 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.021 |  |
| 2025-12-15 12:03:00 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | -0.024 |  |
| 2025-12-15 12:05:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2025-12-15 12:03:23 | Horowpothana (Yan Oya) | 3.97 | 🟢 Normal | -0.038 |  |
| 2025-12-15 12:04:00 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.040 |  |
| 2025-12-15 12:01:56 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)