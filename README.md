# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_17:02:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 17:02:00 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 17:01:44 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:21 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2025-12-14 17:01:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:17 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:10 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:08 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-14 16:13:44 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:11:50 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-14 16:11:04 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.043 |  |
| 2025-12-14 16:09:02 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:08:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 16:07:48 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:07:45 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:07:37 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-14 16:06:58 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.061 |  |
| 2025-12-14 16:06:45 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-14 16:06:26 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 16:06:24 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:05:59 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.029 |  |
| 2025-12-14 16:05:55 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:05:33 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 16:05:01 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:04:57 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:04:42 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:04:38 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.072 |  |
| 2025-12-14 16:04:15 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2025-12-14 16:04:15 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.071 |  |
| 2025-12-14 16:03:54 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2025-12-14 16:03:33 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:03:31 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 17:00:08 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-14 17:02:00 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 16:08:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 16:06:26 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 16:13:44 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:01:46 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:04:57 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:07:45 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:17 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:03:31 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:03:15 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:03:05 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:00:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:09:02 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:44 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:05:01 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-14 17:01:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:05:55 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:07:48 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 16:07:37 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-14 16:11:50 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-14 16:01:28 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-14 16:06:45 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-14 17:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-14 16:02:09 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-14 16:01:45 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.020 |  |
| 2025-12-14 16:01:45 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.020 |  |
| 2025-12-14 16:05:59 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.029 |  |
| 2025-12-14 16:02:09 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.031 |  |
| 2025-12-14 17:01:21 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2025-12-14 16:11:04 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.043 |  |
| 2025-12-14 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.050 |  |
| 2025-12-14 16:06:58 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.061 |  |
| 2025-12-14 16:03:54 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.068 |  |
| 2025-12-14 16:04:15 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.071 |  |
| 2025-12-14 16:04:38 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.072 |  |
| 2025-12-14 16:01:35 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.282 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)