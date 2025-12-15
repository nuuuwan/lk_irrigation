# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_03:04:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 03:04:35 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-16 03:04:11 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 4.390 | 🔺 Rising |
| 2025-12-16 03:03:56 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | -0.039 |  |
| 2025-12-16 03:03:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -10.973 |  |
| 2025-12-16 03:03:06 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:03:05 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2025-12-16 03:02:51 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -10.973 |  |
| 2025-12-16 03:02:49 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 4.390 | 🔺 Rising |
| 2025-12-16 03:02:40 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:37 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -10.973 |  |
| 2025-12-16 03:02:18 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:05 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.030 |  |
| 2025-12-16 03:02:02 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:00 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:01:35 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2025-12-16 03:01:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 03:01:25 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -2.182 |  |
| 2025-12-16 03:00:52 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -2.182 |  |
| 2025-12-16 03:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2025-12-16 02:49:14 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:17:26 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | -0.039 |  |
| 2025-12-16 02:07:21 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-16 02:06:38 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 03:04:11 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 4.390 | 🔺 Rising |
| 2025-12-16 02:07:21 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-16 02:06:38 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 02:04:23 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 03:01:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 03:02:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:01:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:02 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:03:28 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:04:51 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:01:53 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:37 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:49:14 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:02:00 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-16 03:03:06 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:05:57 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:03:40 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:01:25 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 02:04:14 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:05:44 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:06:33 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-16 03:04:35 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 03:03:05 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2025-12-16 01:08:11 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2025-12-16 03:02:05 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.030 |  |
| 2025-12-16 03:01:35 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2025-12-16 01:03:59 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2025-12-16 03:03:56 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | -0.039 |  |
| 2025-12-16 02:05:32 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.050 |  |
| 2025-12-16 03:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |
| 2025-12-16 02:06:14 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -2.057 |  |
| 2025-12-16 03:01:25 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -2.182 |  |
| 2025-12-16 03:03:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -10.973 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)