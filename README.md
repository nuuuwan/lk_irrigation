# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_10:29:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 10:29:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:23:26 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:17:41 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:15:50 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:12:21 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:12:18 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.010 |  |
| 2026-05-29 10:11:32 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-29 10:08:39 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-05-29 10:08:37 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:08:29 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.058 |  |
| 2026-05-29 10:07:57 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.104 |  |
| 2026-05-29 10:07:31 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.075 |  |
| 2026-05-29 10:07:00 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:06:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:05:57 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:05:17 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:05:14 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:05:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-29 10:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 10:04:42 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.029 |  |
| 2026-05-29 10:04:38 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.080 |  |
| 2026-05-29 10:04:38 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:03:47 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:03:35 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:03:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:02:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:02:49 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:02:40 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:02:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:02:27 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.071 |  |
| 2026-05-29 10:02:09 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.061 |  |
| 2026-05-29 10:01:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:01:20 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:01:13 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:01:08 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.065 |  |
| 2026-05-29 10:00:57 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-05-29 10:00:55 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:00:31 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:00:03 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 10:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 10:12:18 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.010 |  |
| 2026-05-29 10:05:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-29 10:11:32 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-29 10:03:35 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:04:38 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:01:20 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:03:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:02:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:08:37 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 10:02:49 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:00:03 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:02:40 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:12:21 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:29:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:02:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:03:47 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:01:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:00:31 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:06:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:07:00 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:23:26 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:17:41 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:15:50 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 10:05:17 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:05:14 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:00:55 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:01:13 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-29 10:00:57 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-05-29 10:04:42 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.029 |  |
| 2026-05-29 10:08:39 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-05-29 10:08:29 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.058 |  |
| 2026-05-29 10:02:09 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.061 |  |
| 2026-05-29 10:01:08 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.065 |  |
| 2026-05-29 10:02:27 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.071 |  |
| 2026-05-29 10:07:31 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.075 |  |
| 2026-05-29 10:04:38 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.080 |  |
| 2026-05-29 10:07:57 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)