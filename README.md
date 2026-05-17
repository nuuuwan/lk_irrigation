# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_12:10:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,276 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 12:10:43 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-17 12:10:04 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:08:47 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.048 |  |
| 2026-05-17 12:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | -0.028 |  |
| 2026-05-17 12:07:17 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:07:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-17 12:06:28 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 12:05:51 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-05-17 12:04:48 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:04:30 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-17 12:04:26 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.106 |  |
| 2026-05-17 12:04:14 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.012 |  |
| 2026-05-17 12:04:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-05-17 12:04:03 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:03:46 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-05-17 12:03:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:03:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:03:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.069 |  |
| 2026-05-17 12:03:11 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 12:02:49 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:38 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-17 12:02:37 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:33 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:33 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-05-17 12:02:31 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.101 |  |
| 2026-05-17 12:02:30 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.047 |  |
| 2026-05-17 12:02:21 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:20 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:15 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:02:09 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:05 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:01:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:01:38 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.064 |  |
| 2026-05-17 12:01:34 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-05-17 12:01:32 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:01:16 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-17 12:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:01:15 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.050 |  |
| 2026-05-17 12:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 12:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | -0.028 |  |
| 2026-05-17 12:07:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-17 12:06:28 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 12:01:58 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:04:48 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:02:15 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 12:04:03 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:03:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:33 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:10:04 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:07:17 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:09 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:03:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:21 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:20 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:37 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:38 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:01:32 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:49 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:02:05 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 12:04:30 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-17 12:10:43 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-17 12:01:16 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-17 12:02:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-17 12:04:14 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.012 |  |
| 2026-05-17 12:02:33 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-05-17 12:05:51 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-05-17 12:04:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-05-17 12:03:11 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 12:01:34 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-05-17 12:03:46 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-05-17 12:02:30 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.047 |  |
| 2026-05-17 12:08:47 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.048 |  |
| 2026-05-17 12:01:15 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.050 |  |
| 2026-05-17 12:01:38 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.064 |  |
| 2026-05-17 12:03:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.069 |  |
| 2026-05-17 12:02:31 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.101 |  |
| 2026-05-17 12:04:26 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)