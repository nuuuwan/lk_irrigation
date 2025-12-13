# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_02:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,270 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 02:16:20 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-14 02:14:41 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -18.000 |  |
| 2025-12-14 02:14:39 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -18.000 |  |
| 2025-12-14 02:14:35 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:14:18 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2025-12-14 02:08:15 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-14 02:07:27 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 02:07:03 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-14 02:06:37 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2025-12-14 02:06:29 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | 3.040 | 🔺 Rising |
| 2025-12-14 02:06:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:04:06 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:03:48 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 02:03:42 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:03:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 02:03:05 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 02:03:05 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-14 02:03:02 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.079 |  |
| 2025-12-14 02:02:56 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:55 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.019 |  |
| 2025-12-14 02:02:54 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:49 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:49 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:38 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:22 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:01:47 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:01:33 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:01:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.157 |  |
| 2025-12-14 02:01:00 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-14 01:52:22 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:49:26 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:47:13 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 02:06:29 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | 3.040 | 🔺 Rising |
| 2025-12-14 02:14:18 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2025-12-14 01:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-14 02:03:05 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-14 02:16:20 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-14 02:08:15 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 02:03:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 01:05:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 02:07:27 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 02:03:48 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 02:03:05 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 02:02:49 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:56 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:01:47 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:01:33 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:04:06 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:02:22 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:47:13 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:14:35 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:06:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 02:07:03 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-14 02:03:42 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:01:00 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:54 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:38 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-14 02:02:49 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-14 01:02:44 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2025-12-14 02:02:55 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.019 |  |
| 2025-12-14 02:06:37 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 01:01:42 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | -0.049 |  |
| 2025-12-14 02:03:02 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.079 |  |
| 2025-12-14 02:01:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.157 |  |
| 2025-12-14 02:14:41 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)