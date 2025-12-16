# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_13:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 13:06:25 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:05:48 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.019 |  |
| 2025-12-16 13:05:44 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:05:16 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:56 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:34 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:30 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:08 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:06 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:03:20 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:03:20 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:03:19 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2025-12-16 13:03:14 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:58 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:02:47 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:45 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:34 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-16 13:02:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-16 13:02:26 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.059 |  |
| 2025-12-16 13:02:25 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-16 13:02:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:23 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 13:02:16 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:11 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:08 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:02:03 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:01:50 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-16 13:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:01:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2025-12-16 13:01:09 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.100 |  |
| 2025-12-16 12:16:57 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:12:04 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2025-12-16 12:11:15 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-16 12:08:15 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.012 |  |
| 2025-12-16 12:08:11 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 13:02:25 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-16 13:02:34 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-16 13:02:23 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 13:02:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:06 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:45 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:08 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:30 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:47 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:03 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:56 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:16 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:08:11 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:06:25 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:16:57 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:05:44 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:05:16 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:19:45 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:03:14 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:02:11 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 13:04:34 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-16 12:12:04 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2025-12-16 13:03:20 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:03:20 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:03:19 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:02:58 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-16 13:02:08 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-16 12:01:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-16 13:01:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2025-12-16 12:08:15 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.012 |  |
| 2025-12-16 13:05:48 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.019 |  |
| 2025-12-16 13:02:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-16 13:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2025-12-16 13:01:50 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-16 13:02:26 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.059 |  |
| 2025-12-16 13:01:09 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)