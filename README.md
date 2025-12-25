# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_10:25:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,406 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 10:25:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.047 |  |
| 2025-12-25 10:17:44 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.114 |  |
| 2025-12-25 10:16:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:16:02 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2025-12-25 10:15:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:15:34 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2025-12-25 10:14:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:13:12 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:12:53 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:11:54 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:08:53 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:45 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.072 |  |
| 2025-12-25 10:06:34 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:30 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:29 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:14 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-25 10:06:00 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:05:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2025-12-25 10:05:27 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.094 |  |
| 2025-12-25 10:05:02 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 10:04:58 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.030 |  |
| 2025-12-25 10:04:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:04:03 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 10:03:43 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 10:03:42 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | -0.124 |  |
| 2025-12-25 10:03:35 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-25 10:03:18 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.295 |  |
| 2025-12-25 10:03:16 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2025-12-25 10:03:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-25 10:02:35 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:29 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 10:02:23 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 10:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:08 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:07 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:05 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:05 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:04 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2025-12-25 10:01:26 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:00:47 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:00:43 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:39:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 10:03:35 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-25 10:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 10:06:14 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-25 10:03:43 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 10:04:03 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 10:02:23 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 10:02:08 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:13:12 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:01:26 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:16:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:00:43 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:05 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:12:53 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:11:54 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:14:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:05 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:07 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:04:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:15:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:34 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:00:47 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:06:30 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:02:29 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:08:53 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:15:34 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2025-12-25 10:03:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-25 10:02:04 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2025-12-25 10:05:02 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 10:04:58 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.030 |  |
| 2025-12-25 10:16:02 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2025-12-25 10:25:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.047 |  |
| 2025-12-25 10:03:16 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2025-12-25 10:05:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2025-12-25 10:06:45 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.072 |  |
| 2025-12-25 10:05:27 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.094 |  |
| 2025-12-25 10:17:44 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.114 |  |
| 2025-12-25 10:03:42 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | -0.124 |  |
| 2025-12-25 10:03:18 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.295 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)