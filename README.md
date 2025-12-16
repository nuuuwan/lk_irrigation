# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_06:28:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 06:28:50 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | -0.018 |  |
| 2025-12-16 06:26:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:12:43 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-16 06:12:17 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:11:35 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:11:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.060 |  |
| 2025-12-16 06:10:24 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:10:10 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -4.696 |  |
| 2025-12-16 06:10:09 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:10:08 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:09:47 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -4.696 |  |
| 2025-12-16 06:09:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -4.696 |  |
| 2025-12-16 06:09:07 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.032 |  |
| 2025-12-16 06:07:46 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:06:43 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:06:29 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 06:06:24 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.022 |  |
| 2025-12-16 06:06:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-16 06:05:40 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-16 06:05:06 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-16 06:04:57 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.057 |  |
| 2025-12-16 06:04:53 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:04:31 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:04:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.046 |  |
| 2025-12-16 06:04:13 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.038 |  |
| 2025-12-16 06:03:58 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2025-12-16 06:03:48 | Horowpothana (Yan Oya) | 3.58 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2025-12-16 06:03:40 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:03:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2025-12-16 06:02:56 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-16 06:02:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:02:42 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2025-12-16 06:02:32 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:02:10 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 06:02:06 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:01:58 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-16 06:01:46 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.064 |  |
| 2025-12-16 06:01:37 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-16 06:01:28 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 05:45:58 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.038 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 06:03:48 | Horowpothana (Yan Oya) | 3.58 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2025-12-16 06:12:43 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-16 06:06:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-16 06:01:37 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-16 06:05:40 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-16 06:02:56 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-16 06:01:28 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 06:02:10 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 06:06:29 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 06:26:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:12:17 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:11:35 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:02:32 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:07:46 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:10:09 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:03:40 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:02:06 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:10:24 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 06:04:53 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:04:31 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:02:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:06:43 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 06:01:58 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-16 06:05:06 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-16 06:28:50 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | -0.018 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 06:06:24 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.022 |  |
| 2025-12-16 06:02:42 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2025-12-16 06:09:07 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.032 |  |
| 2025-12-16 06:03:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2025-12-16 06:04:13 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.038 |  |
| 2025-12-16 06:03:58 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2025-12-16 06:04:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.046 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-16 06:04:57 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.057 |  |
| 2025-12-16 06:11:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.060 |  |
| 2025-12-16 06:01:46 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.064 |  |
| 2025-12-16 06:10:10 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)