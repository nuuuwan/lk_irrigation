# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_19:39:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 19:39:22 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.006 |  |
| 2025-12-13 19:07:48 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:07:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 19:07:27 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-13 19:07:27 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:07:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-13 19:07:14 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:06:39 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:06:12 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 19:05:55 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2025-12-13 19:05:46 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-13 19:05:24 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2025-12-13 19:04:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 19:04:34 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-13 19:03:54 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-13 19:03:01 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-13 19:02:52 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:38 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2025-12-13 19:02:35 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:32 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 19:02:30 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:30 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2025-12-13 19:02:21 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:19 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-13 19:02:04 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:53 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:26 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.040 |  |
| 2025-12-13 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:21 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:18 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:12 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:01 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:00:55 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:00:09 | Horowpothana (Yan Oya) | 5.53 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 19:03:01 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-13 19:07:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-13 19:07:27 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-13 19:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-13 19:05:46 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 19:02:32 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 19:07:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 19:04:58 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 19:06:12 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 19:01:12 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:00:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:07:14 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:30 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:38 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:18 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:04 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:06:19 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:52 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:07:27 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:06:39 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:02:35 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:07:48 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:01:21 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 19:39:22 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.006 |  |
| 2025-12-13 19:05:55 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2025-12-13 19:04:34 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-13 19:03:54 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-13 19:02:19 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:00:55 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:01:01 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-13 19:02:30 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2025-12-13 19:05:24 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2025-12-13 19:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2025-12-13 19:01:26 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.040 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 19:00:09 | Horowpothana (Yan Oya) | 5.53 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)