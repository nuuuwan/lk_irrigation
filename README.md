# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_12:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 12:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:08:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:46 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:12 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:05:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:05:21 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:04:20 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:04:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2025-12-13 12:04:06 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:03:39 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 12:03:33 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:03:31 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2025-12-13 12:03:29 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:03:29 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.044 |  |
| 2025-12-13 12:03:19 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.021 |  |
| 2025-12-13 12:03:18 | Weraganthota (Mahaweli Ganga) | -0.84 | 🟢 Normal | -0.061 |  |
| 2025-12-13 12:03:13 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:03:12 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.138 |  |
| 2025-12-13 12:02:27 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.050 |  |
| 2025-12-13 12:02:12 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:10 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:07 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:01:49 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:43 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.033 |  |
| 2025-12-13 12:01:42 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:40 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-13 12:01:37 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 12:01:35 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.060 |  |
| 2025-12-13 12:01:32 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:01:21 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:01:14 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:01:03 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:00:36 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:00:25 | Horowpothana (Yan Oya) | 5.84 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:00:19 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:00:14 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.055 |  |
| 2025-12-13 11:18:32 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:16:22 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 12:01:37 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 12:03:39 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 12:01:14 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:46 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:05:21 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:27 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:49 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:00:36 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:42 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:05:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:12 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:08:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:03 | Manampitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:10 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:03:33 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:12 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:04:06 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:01:21 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:00:19 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-13 12:01:40 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-13 12:03:31 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2025-12-13 12:03:19 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.021 |  |
| 2025-12-13 12:03:29 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:04:20 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:02:07 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:01:43 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.033 |  |
| 2025-12-13 12:01:32 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:03:13 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:00:25 | Horowpothana (Yan Oya) | 5.84 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:03:29 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.044 |  |
| 2025-12-13 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.050 |  |
| 2025-12-13 12:00:14 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.055 |  |
| 2025-12-13 12:04:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2025-12-13 12:01:35 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.060 |  |
| 2025-12-13 12:03:18 | Weraganthota (Mahaweli Ganga) | -0.84 | 🟢 Normal | -0.061 |  |
| 2025-12-13 12:03:12 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)