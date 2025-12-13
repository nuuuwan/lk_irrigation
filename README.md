# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_16:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 16:11:15 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:08:50 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.028 |  |
| 2025-12-13 16:08:32 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2025-12-13 16:08:13 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-13 16:08:01 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:06:56 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-13 16:06:50 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:05:39 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:05:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 16:05:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 16:04:51 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.029 |  |
| 2025-12-13 16:04:37 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:04:37 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:04:25 | Kithulgala (Kelani Ganga) | 0.75 | 🟢 Normal | -21.111 |  |
| 2025-12-13 16:04:11 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.050 |  |
| 2025-12-13 16:04:00 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2025-12-13 16:03:33 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.011 |  |
| 2025-12-13 16:03:05 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 16:02:54 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:46 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.090 |  |
| 2025-12-13 16:02:46 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:02:37 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:30 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:24 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.083 |  |
| 2025-12-13 16:02:10 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.052 |  |
| 2025-12-13 16:02:02 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:48 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -21.111 |  |
| 2025-12-13 16:01:40 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:08 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:01:07 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:00:52 | Horowpothana (Yan Oya) | 5.67 | 🟢 Normal | -0.040 |  |
| 2025-12-13 16:00:52 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.083 |  |
| 2025-12-13 16:00:37 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:00:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 16:03:05 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-13 16:05:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 16:05:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 16:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:02 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:54 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:11:15 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:40 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:30 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:07 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:06:50 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:01:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:00:37 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:04:37 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:37 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:46 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:05:39 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:04:37 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:08:13 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-13 16:08:32 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2025-12-13 16:08:01 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:01:48 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:02:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:01:08 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:00:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:02:24 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2025-12-13 16:03:33 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.011 |  |
| 2025-12-13 16:06:56 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-13 16:04:00 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2025-12-13 16:08:50 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.028 |  |
| 2025-12-13 16:04:51 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.029 |  |
| 2025-12-13 16:00:52 | Horowpothana (Yan Oya) | 5.67 | 🟢 Normal | -0.040 |  |
| 2025-12-13 15:08:30 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.049 |  |
| 2025-12-13 16:04:11 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.050 |  |
| 2025-12-13 16:02:10 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.052 |  |
| 2025-12-13 16:00:52 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.083 |  |
| 2025-12-13 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.083 |  |
| 2025-12-13 16:02:46 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.090 |  |
| 2025-12-13 16:04:25 | Kithulgala (Kelani Ganga) | 0.75 | 🟢 Normal | -21.111 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)