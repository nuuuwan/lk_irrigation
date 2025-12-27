# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_11:06:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 11:06:05 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2025-12-27 11:05:59 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:05:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:05:11 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 11:05:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2025-12-27 11:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:04:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:04:17 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2025-12-27 11:04:16 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:04:12 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2025-12-27 11:03:55 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:03:40 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:03:36 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:03:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:03:26 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-27 11:03:04 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:03:03 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 11:03:03 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.082 |  |
| 2025-12-27 11:03:02 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-27 11:02:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:30 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:18 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:01:54 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:01:39 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2025-12-27 11:01:34 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2025-12-27 11:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:00:48 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.038 |  |
| 2025-12-27 11:00:47 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2025-12-27 11:00:44 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:00:44 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:25:11 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2025-12-27 10:16:50 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-27 10:13:22 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.038 |  |
| 2025-12-27 10:10:15 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-27 10:09:50 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 11:01:39 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2025-12-27 09:13:18 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-27 11:03:02 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-27 11:03:03 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 10:03:17 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 11:05:11 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 11:03:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:09 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:30 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:00:44 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:03:04 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:01:54 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:05:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:04:16 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:02:18 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 10:09:50 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:03:40 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:04:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 11:01:34 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2025-12-27 11:03:36 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:03:55 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:00:44 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:05:59 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:35 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-27 11:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-27 10:05:18 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-27 11:04:12 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2025-12-27 11:06:05 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2025-12-27 10:05:54 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2025-12-27 11:04:17 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2025-12-27 11:00:47 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2025-12-27 11:00:48 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.038 |  |
| 2025-12-27 11:03:26 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-27 11:05:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2025-12-27 11:03:03 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.082 |  |
| 2025-12-27 10:00:38 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.310 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)