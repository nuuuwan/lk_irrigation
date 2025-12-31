# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_22:20:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 22:20:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 22:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2025-12-31 22:09:27 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:09:23 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-31 22:08:39 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:08:10 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:07:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-31 22:06:34 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-31 22:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-31 22:05:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:05:08 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:05:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-31 22:05:08 | Siyambalanduwa (Heda Oya) | 3.62 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2025-12-31 22:04:30 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-31 22:04:28 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:04:02 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:04:00 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:03:54 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-31 22:03:51 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:03:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:02:55 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:02:53 | Katharagama (Menik Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:02:42 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:02:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 22:02:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.049 |  |
| 2025-12-31 22:01:56 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-31 22:01:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:01:48 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2025-12-31 22:01:28 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | -1.255 |  |
| 2025-12-31 22:01:28 | Kuda Oya (Kirindi Oya) | 2.40 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2025-12-31 22:01:28 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:01:13 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 22:05:08 | Siyambalanduwa (Heda Oya) | 3.62 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2025-12-31 22:01:28 | Kuda Oya (Kirindi Oya) | 2.40 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2025-12-31 22:03:54 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-31 22:01:48 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2025-12-31 22:04:30 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-31 22:06:34 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-31 22:05:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-31 22:09:23 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-31 22:01:56 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-31 22:07:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-31 21:09:15 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 22:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 22:02:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 22:01:13 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 22:05:08 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:02:53 | Katharagama (Menik Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 22:05:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:02:42 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:04:02 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:04:00 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:01:49 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:09:27 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:08:39 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:08:10 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:29 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:03:51 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:05:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 22:20:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2025-12-31 22:03:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:02:55 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:01:28 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2025-12-31 22:02:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.049 |  |
| 2025-12-31 22:01:28 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | -1.255 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)