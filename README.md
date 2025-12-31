# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_20:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 20:14:23 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:13:05 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:12:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 20:11:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:11:00 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:09:26 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:07:48 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.039 |  |
| 2025-12-31 20:07:31 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:06:58 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:06:48 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.124 |  |
| 2025-12-31 20:06:06 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:05:53 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.078 |  |
| 2025-12-31 20:05:48 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 20:05:36 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.360 | 🔺 Rising |
| 2025-12-31 20:05:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:04:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 20:04:08 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 20:03:59 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:03:47 | Nakkala (Kumbukkan Oya) | 3.90 | 🟢 Normal | -0.063 |  |
| 2025-12-31 20:03:30 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:03:10 | Siyambalanduwa (Heda Oya) | 2.86 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2025-12-31 20:03:02 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:50 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:47 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-31 20:02:40 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:37 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 20:02:33 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:26 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:21 | Katharagama (Menik Ganga) | 1.35 | 🟢 Normal | 1.103 | 🔺 Rising |
| 2025-12-31 20:02:18 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 20:02:13 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 20:02:13 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:07 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:04 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:01:28 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -2.000 |  |
| 2025-12-31 20:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -2.000 |  |
| 2025-12-31 20:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 19:42:02 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 19:22:02 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 20:02:21 | Katharagama (Menik Ganga) | 1.35 | 🟢 Normal | 1.103 | 🔺 Rising |
| 2025-12-31 20:03:10 | Siyambalanduwa (Heda Oya) | 2.86 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2025-12-31 20:05:36 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.360 | 🔺 Rising |
| 2025-12-31 20:02:47 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-31 20:12:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 20:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 20:04:08 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 20:02:37 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 20:05:48 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 20:02:18 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 20:04:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 20:02:13 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 20:11:00 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:01:28 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:14:23 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:09:26 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:13 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:33 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:40 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:06:58 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:03:02 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:07:31 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:05:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:06:06 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:02:04 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:11:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 20:13:05 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:26 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:03:59 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:07 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:02:50 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-31 20:07:48 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.039 |  |
| 2025-12-31 20:03:47 | Nakkala (Kumbukkan Oya) | 3.90 | 🟢 Normal | -0.063 |  |
| 2025-12-31 20:05:53 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.078 |  |
| 2025-12-31 20:06:48 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.124 |  |
| 2025-12-31 20:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)