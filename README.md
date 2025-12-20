# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_01:12:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 01:12:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:08:26 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:07:23 | Manampitiya (Mahaweli Ganga) | 3.41 | 🟡 Alert | -0.010 |  |
| 2025-12-21 01:06:38 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-21 01:05:39 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-21 01:05:22 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 01:05:20 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:11 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2025-12-21 01:05:04 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:04:44 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-21 01:04:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:04:25 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:04:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:03:05 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-21 01:02:55 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-21 01:02:42 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:02:33 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-21 01:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.063 |  |
| 2025-12-21 01:02:13 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:02:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:57 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:53 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-21 01:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-21 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2025-12-21 01:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 01:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:05 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:33:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.063 |  |
| 2025-12-21 00:20:53 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-21 00:18:48 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 01:07:23 | Manampitiya (Mahaweli Ganga) | 3.41 | 🟡 Alert | -0.010 |  |
| 2025-12-21 00:02:10 | Horowpothana (Yan Oya) | 6.13 | 🟡 Alert | -0.046 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-21 00:06:02 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-21 01:01:53 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-21 00:09:00 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-21 01:02:33 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-21 01:01:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 01:06:38 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 01:05:39 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-21 01:05:22 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 01:04:44 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 01:04:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:00:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:57 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:02:13 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:04 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:04:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:04:25 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:06:21 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:12:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:02:42 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:02:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:05 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:20 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:08:26 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-21 01:03:05 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-21 00:02:20 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.013 |  |
| 2025-12-21 01:05:11 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2025-12-21 01:02:55 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-21 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2025-12-21 01:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)