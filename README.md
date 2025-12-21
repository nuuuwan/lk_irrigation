# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_22:30:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 22:30:16 | Horowpothana (Yan Oya) | 4.42 | 🟢 Normal | -0.052 |  |
| 2025-12-21 22:23:40 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.023 |  |
| 2025-12-21 22:21:58 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:21:19 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:20:14 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:19:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2025-12-21 22:11:24 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:07:40 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.039 |  |
| 2025-12-21 22:06:48 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.024 |  |
| 2025-12-21 22:06:30 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:06:19 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-21 22:06:04 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 22:06:00 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:05:57 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.005 |  |
| 2025-12-21 22:05:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-21 22:05:34 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:05:00 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-21 22:04:22 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-21 22:03:42 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-21 22:03:33 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2025-12-21 22:03:12 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:03:02 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-21 22:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:02:46 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:02:36 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-21 22:01:27 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 22:01:26 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:01:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 22:01:04 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:00:27 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:00:26 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.051 |  |
| 2025-12-21 22:00:13 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 22:05:00 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 22:06:19 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-21 22:03:02 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-21 22:06:04 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 22:03:42 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-21 22:01:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 21:01:32 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 22:01:27 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 22:00:27 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:01:04 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:01:26 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:07:04 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:00:13 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:21:19 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:03:12 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:03:33 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:04:54 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:02:46 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:11:24 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:02:30 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:06:30 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:06:00 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:21:58 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:05:34 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:05:57 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.005 |  |
| 2025-12-21 22:19:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2025-12-21 22:02:36 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-21 22:04:22 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 22:23:40 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.023 |  |
| 2025-12-21 22:06:48 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.024 |  |
| 2025-12-21 22:05:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-21 22:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2025-12-21 22:07:40 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.039 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 22:00:26 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.051 |  |
| 2025-12-21 22:30:16 | Horowpothana (Yan Oya) | 4.42 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)