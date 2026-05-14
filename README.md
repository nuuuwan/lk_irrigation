# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_21:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 21:11:29 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:11:00 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-14 21:08:01 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 21:07:28 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.099 |  |
| 2026-05-14 21:06:13 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:06:11 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:06:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-14 21:06:03 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-05-14 21:05:50 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:05:19 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.038 |  |
| 2026-05-14 21:04:57 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-14 21:04:51 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:04:51 | Deraniyagala (Kelani Ganga) | 2.56 | 🟢 Normal | -0.459 |  |
| 2026-05-14 21:04:38 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 21:04:29 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-05-14 21:04:26 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:04:14 | Glencourse (Kelani Ganga) | 13.73 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-05-14 21:04:04 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-14 21:04:00 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:03:23 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-14 21:03:20 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 21:03:16 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 21:02:54 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 21:02:45 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:43 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-05-14 21:02:29 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-05-14 21:02:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:16 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:01:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.084 |  |
| 2026-05-14 21:01:40 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:01:16 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:00:17 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-14 21:00:16 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:00:12 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 20:34:48 | Deraniyagala (Kelani Ganga) | 2.79 | 🟢 Normal | -0.459 |  |
| 2026-05-14 20:33:48 | Deraniyagala (Kelani Ganga) | 2.79 | 🟢 Normal | -0.459 |  |
| 2026-05-14 20:33:46 | Deraniyagala (Kelani Ganga) | 3.05 | 🟢 Normal | -0.459 |  |
| 2026-05-14 20:33:44 | Deraniyagala (Kelani Ganga) | 3.40 | 🟢 Normal | -0.459 |  |
| 2026-05-14 20:33:42 | Deraniyagala (Kelani Ganga) | 3.65 | 🟢 Normal | -0.459 |  |
| 2026-05-14 20:33:39 | Deraniyagala (Kelani Ganga) | 3.65 | 🟢 Normal | -0.459 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 20:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-14 21:06:03 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-05-14 21:03:23 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-14 21:02:43 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-05-14 21:04:14 | Glencourse (Kelani Ganga) | 13.73 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-05-14 21:06:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-14 21:04:04 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-14 21:11:00 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-14 21:00:17 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-14 21:04:57 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-14 21:03:20 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 21:04:38 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 21:02:54 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 21:03:16 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 21:00:12 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 21:01:40 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:04:51 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:02:16 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:11:29 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:06:13 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:04:26 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:05:50 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 21:04:00 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:29 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:00:16 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:06:11 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:01:16 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:45 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:02:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-14 21:08:01 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 21:04:29 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-05-14 21:05:19 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.038 |  |
| 2026-05-14 21:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-05-14 21:01:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.084 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 21:07:28 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.099 |  |
| 2026-05-14 21:04:51 | Deraniyagala (Kelani Ganga) | 2.56 | 🟢 Normal | -0.459 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)