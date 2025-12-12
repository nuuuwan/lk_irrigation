# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_07:19:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 07:19:22 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:16:53 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | -0.008 |  |
| 2025-12-12 07:16:25 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2025-12-12 07:13:13 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.113 |  |
| 2025-12-12 07:13:05 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | -0.017 |  |
| 2025-12-12 07:11:55 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 07:10:14 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 07:08:35 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:07:08 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2025-12-12 07:06:41 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.183 |  |
| 2025-12-12 07:06:40 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:06:31 | Thanthirimale (Malwathu Oya) | 4.19 | 🟢 Normal | -0.001 |  |
| 2025-12-12 07:06:24 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 07:05:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.066 |  |
| 2025-12-12 07:05:06 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-12 07:04:55 | Horowpothana (Yan Oya) | 5.06 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-12 07:04:49 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-12 07:04:35 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:04:33 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-12 07:04:17 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-12 07:04:13 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.022 |  |
| 2025-12-12 07:04:09 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.038 |  |
| 2025-12-12 07:03:57 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:03:51 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-12 07:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -3.288 |  |
| 2025-12-12 07:03:36 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:03:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 07:03:17 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-12 07:03:12 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2025-12-12 07:02:53 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-12 07:02:46 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-12 07:02:43 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.087 |  |
| 2025-12-12 07:02:31 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.049 |  |
| 2025-12-12 07:01:50 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.022 |  |
| 2025-12-12 07:01:20 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-12 07:00:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2025-12-12 06:37:40 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | -0.017 |  |
| 2025-12-12 06:27:05 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 07:04:55 | Horowpothana (Yan Oya) | 5.06 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 07:01:20 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-12 07:04:49 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-12 07:03:51 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-12 07:05:06 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-12 07:02:53 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-12 07:10:14 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 07:11:55 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 07:06:24 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 07:03:33 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 07:04:33 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 07:06:40 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:19:22 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:03:57 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:03:36 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:08:35 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:04:35 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 07:06:31 | Thanthirimale (Malwathu Oya) | 4.19 | 🟢 Normal | -0.001 |  |
| 2025-12-12 07:16:53 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | -0.008 |  |
| 2025-12-12 07:04:17 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-12 07:02:46 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-12 07:03:17 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-12 07:13:05 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | -0.017 |  |
| 2025-12-12 07:00:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2025-12-12 07:01:50 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.022 |  |
| 2025-12-12 07:04:13 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.022 |  |
| 2025-12-12 07:03:12 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2025-12-12 07:04:09 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.038 |  |
| 2025-12-12 06:07:56 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2025-12-12 07:02:31 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.049 |  |
| 2025-12-12 07:07:08 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2025-12-12 07:16:25 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2025-12-12 07:05:26 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.066 |  |
| 2025-12-12 07:02:43 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.087 |  |
| 2025-12-12 07:13:13 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.113 |  |
| 2025-12-12 07:06:41 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.183 |  |
| 2025-12-12 07:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -3.288 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)