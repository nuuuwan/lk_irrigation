# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_06:32:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,328 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 06:32:52 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.007 |  |
| 2025-12-15 06:13:36 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-15 06:12:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:12:15 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:11:25 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:11:20 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.011 |  |
| 2025-12-15 06:10:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2025-12-15 06:09:38 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2025-12-15 06:09:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.103 |  |
| 2025-12-15 06:08:51 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.034 |  |
| 2025-12-15 06:08:31 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:08:21 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:07:34 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.078 |  |
| 2025-12-15 06:07:19 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-15 06:06:37 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:06:33 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-15 06:06:21 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2025-12-15 06:06:16 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.019 |  |
| 2025-12-15 06:05:22 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-15 06:05:17 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.062 |  |
| 2025-12-15 06:04:39 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:20 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:11 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:08 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 06:04:05 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 06:03:48 | Horowpothana (Yan Oya) | 4.14 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:03:46 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:03:02 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:02:42 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.023 |  |
| 2025-12-15 06:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:26 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:22 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:20 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 06:02:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:01:49 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-15 06:01:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:01:12 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:00:44 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:56:10 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 06:10:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2025-12-15 06:13:36 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-15 06:02:20 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 06:04:08 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 06:08:31 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:00:44 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:11 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:12:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:01:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:20 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:02:22 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:06:37 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:08:21 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:04:39 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:12:15 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:11:25 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 06:05:22 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-15 06:32:52 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.007 |  |
| 2025-12-15 06:07:19 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-15 06:03:02 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:03:48 | Horowpothana (Yan Oya) | 4.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:03:46 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:01:12 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-15 06:11:20 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.011 |  |
| 2025-12-15 06:06:16 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.019 |  |
| 2025-12-15 06:04:05 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 06:02:42 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.023 |  |
| 2025-12-15 06:06:33 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-15 06:01:49 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-15 06:08:51 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.034 |  |
| 2025-12-15 06:06:21 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2025-12-15 06:05:17 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.062 |  |
| 2025-12-15 06:07:34 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.078 |  |
| 2025-12-15 06:09:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)