# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_06:33:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 06:33:18 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.003 |  |
| 2025-12-14 06:27:57 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:18:22 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:18:15 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:16:59 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-14 06:16:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 3.295 | 🔺 Rising |
| 2025-12-14 06:11:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 3.295 | 🔺 Rising |
| 2025-12-14 06:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | 3.295 | 🔺 Rising |
| 2025-12-14 06:11:12 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-14 06:11:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | 3.295 | 🔺 Rising |
| 2025-12-14 06:09:47 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:09:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.024 |  |
| 2025-12-14 06:06:38 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:24 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:24 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:23 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.237 |  |
| 2025-12-14 06:06:03 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.039 |  |
| 2025-12-14 06:06:00 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:05:49 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 06:05:33 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-14 06:05:01 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:54 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2025-12-14 06:04:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:14 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:13 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 06:03:53 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-14 06:03:19 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:03:15 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2025-12-14 06:02:59 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-14 06:02:50 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.213 |  |
| 2025-12-14 06:02:42 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-14 06:02:41 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 06:02:35 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:02:26 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.055 |  |
| 2025-12-14 06:02:17 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:02:14 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.022 |  |
| 2025-12-14 06:02:05 | Horowpothana (Yan Oya) | 4.87 | 🟢 Normal | -0.124 |  |
| 2025-12-14 06:01:10 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:01:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2025-12-14 06:01:00 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.103 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 06:16:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 3.295 | 🔺 Rising |
| 2025-12-14 06:02:59 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-14 06:11:12 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-14 06:01:00 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-14 06:02:42 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 06:16:59 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-14 06:05:49 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 06:02:41 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 06:33:18 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.003 |  |
| 2025-12-14 06:02:17 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:02:35 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:18:15 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:27:57 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:24 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:18:22 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:00 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:14 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:03:19 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:05:01 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:09:47 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:01:10 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:06:38 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:04:13 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 06:03:53 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:05:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 06:05:33 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-14 06:04:54 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2025-12-14 06:02:14 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.022 |  |
| 2025-12-14 06:09:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.024 |  |
| 2025-12-14 06:06:03 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.039 |  |
| 2025-12-14 06:03:15 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 06:02:26 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.055 |  |
| 2025-12-14 06:01:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2025-12-14 06:02:05 | Horowpothana (Yan Oya) | 4.87 | 🟢 Normal | -0.124 |  |
| 2025-12-14 06:02:50 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.213 |  |
| 2025-12-14 06:06:23 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)