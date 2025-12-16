# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_14:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 14:11:49 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.048 |  |
| 2025-12-16 14:10:43 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:09:22 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 14:08:58 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:08:42 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:07:12 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:07:12 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:06:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 14:05:47 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:05:34 | Thanthirimale (Malwathu Oya) | 3.55 | 🟢 Normal | -0.067 |  |
| 2025-12-16 14:05:23 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-16 14:04:51 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:04:29 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:04:26 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-16 14:04:10 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:04:05 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 14:03:59 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:27 | Horowpothana (Yan Oya) | 5.57 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-16 14:03:08 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:05 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:02:56 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:02:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2025-12-16 14:02:48 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:02:27 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:02:24 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:02:19 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:46 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:01:38 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.005 |  |
| 2025-12-16 14:01:35 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2025-12-16 14:01:31 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:26 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:25 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:10 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | -0.070 |  |
| 2025-12-16 14:01:05 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:00:48 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:59:54 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 14:05:23 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-16 14:03:27 | Horowpothana (Yan Oya) | 5.57 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-16 14:09:22 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 14:04:05 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 14:06:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 14:01:38 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.005 |  |
| 2025-12-16 14:04:10 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:02:19 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:59 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:04:29 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:26 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:02:24 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:05 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:07:12 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:02:48 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:00:48 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:25 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:01:31 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:05 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:08 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:04:26 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:08:58 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:08:42 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:10:43 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:05:47 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:04:51 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:07:12 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:02:27 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:02:56 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:01:46 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:03:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-16 14:01:35 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2025-12-16 14:11:49 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.048 |  |
| 2025-12-16 14:02:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2025-12-16 14:05:34 | Thanthirimale (Malwathu Oya) | 3.55 | 🟢 Normal | -0.067 |  |
| 2025-12-16 14:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-16 14:01:10 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)