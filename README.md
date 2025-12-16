# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_12:16:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 12:16:57 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:12:04 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2025-12-16 12:11:15 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-16 12:08:15 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.012 |  |
| 2025-12-16 12:08:11 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:07:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:06:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2025-12-16 12:06:37 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:06:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:05:45 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.048 |  |
| 2025-12-16 12:04:55 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:51 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:47 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:37 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:34 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:04:32 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:18 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:04:10 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:04:01 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2025-12-16 12:03:54 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:03:50 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:03:38 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:03:07 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.094 |  |
| 2025-12-16 12:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:02:51 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:44 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 12:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:29 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:27 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 12:02:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-16 12:02:11 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:53 | Thanthirimale (Malwathu Oya) | 3.68 | 🟢 Normal | -0.071 |  |
| 2025-12-16 12:01:51 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:47 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:01:26 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-16 12:01:18 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-16 12:01:13 | Yaka Wewa (Ma Oya) | 1.75 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 12:02:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-16 12:01:18 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-16 12:01:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-16 12:11:15 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-16 12:02:27 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 12:02:44 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 12:04:47 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:26 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:03:50 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:51 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:51 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:32 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:29 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:55 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:07:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:01:47 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:06:37 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:04:37 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:08:11 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:06:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:16:57 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:19:45 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:02:11 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:12:04 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2025-12-16 12:03:38 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:04:10 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:04:18 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:01:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:03:54 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:04:34 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:08:15 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.012 |  |
| 2025-12-16 12:06:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2025-12-16 12:04:01 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2025-12-16 12:05:45 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.048 |  |
| 2025-12-16 12:01:53 | Thanthirimale (Malwathu Oya) | 3.68 | 🟢 Normal | -0.071 |  |
| 2025-12-16 12:01:13 | Yaka Wewa (Ma Oya) | 1.75 | 🟢 Normal | -0.081 |  |
| 2025-12-16 12:03:07 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)