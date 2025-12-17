# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_08:12:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,204 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 08:12:56 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2025-12-17 08:11:31 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:11:22 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2025-12-17 08:07:51 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-17 08:06:37 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 08:06:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:06:03 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:04:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2025-12-17 08:04:48 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.283 |  |
| 2025-12-17 08:04:41 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:04:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 08:04:25 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.176 |  |
| 2025-12-17 08:04:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:04:04 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:04:03 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 08:03:29 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:03:28 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-17 08:03:17 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.040 |  |
| 2025-12-17 08:03:12 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:03:10 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 08:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.090 |  |
| 2025-12-17 08:02:35 | Thanthirimale (Malwathu Oya) | 3.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 08:02:33 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:31 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.036 |  |
| 2025-12-17 08:02:06 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:50 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 08:01:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:39 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:25 | Horowpothana (Yan Oya) | 5.94 | 🟢 Normal | -0.046 |  |
| 2025-12-17 08:01:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-17 08:01:10 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:00:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.046 |  |
| 2025-12-17 07:53:15 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 08:07:51 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-17 08:02:35 | Thanthirimale (Malwathu Oya) | 3.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 08:06:37 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 08:03:10 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 08:04:03 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 08:03:28 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-17 08:01:50 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 08:04:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 08:04:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:33 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:39 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:03:29 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:31 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:06:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:03:12 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:11:31 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:06:03 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:04:41 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:04:04 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-17 08:11:22 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2025-12-17 08:01:10 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-17 08:12:56 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2025-12-17 08:02:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.036 |  |
| 2025-12-17 08:04:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2025-12-17 08:03:17 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.040 |  |
| 2025-12-17 08:01:25 | Horowpothana (Yan Oya) | 5.94 | 🟢 Normal | -0.046 |  |
| 2025-12-17 08:00:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.046 |  |
| 2025-12-17 08:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.090 |  |
| 2025-12-17 08:04:25 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.176 |  |
| 2025-12-17 08:04:48 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.283 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)