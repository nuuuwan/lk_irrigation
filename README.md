# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_16:17:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 16:17:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-26 16:14:18 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.016 |  |
| 2025-12-26 16:12:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-26 16:10:55 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:10:27 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2025-12-26 16:09:48 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2025-12-26 16:09:21 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:09:05 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:08:42 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:07:04 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:06:33 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:06:33 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:06:30 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:05:14 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:05:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:05:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-26 16:04:44 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:04:42 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:04:13 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:04:04 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.021 |  |
| 2025-12-26 16:03:51 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:48 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:43 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-26 16:03:34 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:24 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:03:22 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:58 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:44 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.050 |  |
| 2025-12-26 16:02:40 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 16:02:32 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:16 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.023 |  |
| 2025-12-26 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.080 |  |
| 2025-12-26 16:02:08 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:01:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:01:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2025-12-26 16:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:00:50 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:00:28 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.012 |  |
| 2025-12-26 16:00:16 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 15:02:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-26 16:03:43 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-26 16:02:40 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 16:17:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-26 16:04:44 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:05:14 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:58 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:04:13 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:03:24 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:01:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:00:16 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:10:55 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:32 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:06:30 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:02:08 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:08:42 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:06:33 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:09:05 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:09:21 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 16:12:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-26 16:05:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-26 16:07:04 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:51 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:04:42 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:06:33 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:00:50 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:05:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:48 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:03:34 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 16:00:28 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.012 |  |
| 2025-12-26 16:14:18 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.016 |  |
| 2025-12-26 16:09:48 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2025-12-26 16:04:04 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.021 |  |
| 2025-12-26 16:02:16 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.023 |  |
| 2025-12-26 16:10:27 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2025-12-26 16:01:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2025-12-26 16:02:44 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.050 |  |
| 2025-12-26 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)