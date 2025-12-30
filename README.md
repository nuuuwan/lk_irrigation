# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_21:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,263 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 21:18:39 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:11:08 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.017 |  |
| 2025-12-30 21:10:33 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:08:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 21:07:37 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-30 21:06:23 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:47 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2025-12-30 21:05:37 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:32 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:05:19 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:03 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2025-12-30 21:04:22 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:09 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:09 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:04:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-30 21:03:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-30 21:03:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:03:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:15 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-30 21:02:39 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:02:36 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-30 21:02:26 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:59 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-30 21:01:41 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-30 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:07 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:00:56 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-30 21:00:28 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:00:11 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 20:29:00 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 21:00:56 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-30 21:03:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-30 20:07:47 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-30 21:03:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-30 21:02:36 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-30 21:01:59 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:04:09 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:05:32 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:03:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 21:08:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 21:01:41 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:11 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:22 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:00:28 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:10:33 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:18:39 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:02:26 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:07 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:19 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:00:11 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:06:23 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:09 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:05:37 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:02:39 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:15 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-30 21:07:37 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-30 21:11:08 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.017 |  |
| 2025-12-30 21:05:03 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2025-12-30 21:05:47 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2025-12-30 21:01:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-30 20:16:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)