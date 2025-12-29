# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_14:10:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 14:10:47 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-29 14:10:39 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:09:42 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:08:24 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:07:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2025-12-29 14:06:50 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:06:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2025-12-29 14:05:46 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:05:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 14:05:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:05:15 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 14:05:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-29 14:05:02 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.024 |  |
| 2025-12-29 14:04:55 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:04:31 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 14:04:24 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.097 |  |
| 2025-12-29 14:03:38 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:03:11 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:03:11 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.063 |  |
| 2025-12-29 14:03:06 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:56 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:41 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:38 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:36 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:25 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.032 |  |
| 2025-12-29 14:02:22 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:12 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-29 14:02:04 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 14:01:41 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 14:01:26 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-29 14:01:23 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:01:23 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.020 |  |
| 2025-12-29 14:01:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.197 |  |
| 2025-12-29 14:00:53 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:00:50 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:00:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-29 14:00:09 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 14:01:41 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 14:05:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 14:02:04 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 14:04:31 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 14:05:15 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 14:05:46 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:04:55 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:00:53 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:05:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:12:11 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:10:39 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:03:38 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:41 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:22 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:06:50 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:09:42 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:03:11 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:00:50 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:36 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:03:06 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:08:24 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:01:23 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:02:56 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 14:07:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2025-12-29 14:10:47 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-29 14:02:12 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-29 14:01:26 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-29 14:00:09 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2025-12-29 14:06:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2025-12-29 14:01:23 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.020 |  |
| 2025-12-29 14:05:02 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.024 |  |
| 2025-12-29 14:05:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-29 14:00:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-29 14:02:25 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.032 |  |
| 2025-12-29 14:03:11 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.063 |  |
| 2025-12-29 14:04:24 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.097 |  |
| 2025-12-29 14:01:13 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)