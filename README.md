# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_07:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,172 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 07:18:39 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:12:05 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.017 |  |
| 2025-12-26 07:10:42 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.026 |  |
| 2025-12-26 07:10:10 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2025-12-26 07:07:51 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-26 07:07:31 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-26 07:07:24 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:07:14 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:07:05 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.028 |  |
| 2025-12-26 07:06:49 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:06:37 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.056 |  |
| 2025-12-26 07:06:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.092 |  |
| 2025-12-26 07:06:06 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:04:47 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:41 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-26 07:04:34 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:04:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:25 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:04:25 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:22 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-26 07:04:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:04:04 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.012 |  |
| 2025-12-26 07:04:02 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-26 07:04:00 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.043 |  |
| 2025-12-26 07:04:00 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:03:58 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2025-12-26 07:02:38 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:02:27 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:02:18 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:01:43 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:01:17 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:01:17 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:01:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:00:38 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:00:37 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2025-12-26 06:38:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:36:29 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 07:07:51 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-26 07:04:02 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-26 07:04:22 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-26 07:07:31 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-26 07:04:25 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:04:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 07:01:17 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:02:27 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:18:39 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:01:43 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:47 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:07:24 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:00 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:02:18 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:00:38 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:04:25 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:02:38 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:06:49 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 07:07:14 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:04:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:01:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:04:34 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:01:17 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:06:06 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-26 07:00:37 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2025-12-26 07:04:04 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.012 |  |
| 2025-12-26 06:20:28 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.017 |  |
| 2025-12-26 07:12:05 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.017 |  |
| 2025-12-26 07:04:41 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-26 06:05:38 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-26 07:10:42 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.026 |  |
| 2025-12-26 07:07:05 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.028 |  |
| 2025-12-26 07:10:10 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2025-12-26 07:03:58 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2025-12-26 07:04:00 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.043 |  |
| 2025-12-26 07:06:37 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.056 |  |
| 2025-12-26 07:06:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)