# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_17:17:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,860 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 17:17:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-14 17:10:42 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.038 |  |
| 2025-12-14 17:09:45 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-14 17:06:37 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:05:46 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-14 17:05:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:05:10 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:05:08 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.020 |  |
| 2025-12-14 17:05:03 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2025-12-14 17:04:41 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.022 |  |
| 2025-12-14 17:04:27 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-14 17:04:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:04:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:04:02 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 17:03:33 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:03:22 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2025-12-14 17:03:22 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:03:14 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.081 |  |
| 2025-12-14 17:03:05 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:02:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:02:50 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.029 |  |
| 2025-12-14 17:02:38 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:38 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:27 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.032 |  |
| 2025-12-14 17:02:26 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:26 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:20 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.050 |  |
| 2025-12-14 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.050 |  |
| 2025-12-14 17:02:17 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 17:02:15 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2025-12-14 17:02:00 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 17:01:44 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:21 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2025-12-14 17:01:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:17 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:10 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:08 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 17:05:03 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2025-12-14 17:05:46 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-14 17:00:08 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-14 17:17:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-14 17:02:00 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 17:02:17 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 17:04:02 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 17:04:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:26 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:03:22 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:04:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:38 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:38 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:17 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:03:33 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:02:26 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:44 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:05:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:03:05 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:05:10 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:02:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:06:37 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:03:22 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2025-12-14 17:04:27 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2025-12-14 17:09:45 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2025-12-14 17:05:08 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.020 |  |
| 2025-12-14 17:04:41 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.022 |  |
| 2025-12-14 17:02:50 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.029 |  |
| 2025-12-14 17:02:15 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2025-12-14 17:01:21 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2025-12-14 17:02:27 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.032 |  |
| 2025-12-14 17:10:42 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.038 |  |
| 2025-12-14 17:02:20 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.050 |  |
| 2025-12-14 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.050 |  |
| 2025-12-14 17:03:14 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)