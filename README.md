# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_10:27:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,773 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 10:27:20 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:18:59 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-26 10:11:08 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.035 |  |
| 2026-06-26 10:08:34 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:08:04 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.048 |  |
| 2026-06-26 10:08:04 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:07:47 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:06:51 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.038 |  |
| 2026-06-26 10:06:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:06:39 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 10:06:31 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -58.852 |  |
| 2026-06-26 10:06:25 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-26 10:04:36 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -58.852 |  |
| 2026-06-26 10:04:36 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-06-26 10:04:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-26 10:04:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:04:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:04:05 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:31 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-26 10:03:30 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:03:20 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:11 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-26 10:02:59 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:02:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-26 10:02:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:02:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:02:22 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-26 10:02:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.246 |  |
| 2026-06-26 10:02:01 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.011 |  |
| 2026-06-26 10:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:01:30 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:00:56 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:00:49 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:00:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:00:11 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-26 10:00:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 10:02:22 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-26 10:03:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-26 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-26 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-26 10:02:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 10:01:30 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:03:30 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:02:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 10:06:39 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-26 10:18:59 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-26 10:00:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:08:04 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:04:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:20 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:10:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:04:05 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:02:59 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:00:56 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:11 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:06:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:06:25 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:08:34 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:00:49 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:07:47 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:27:20 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:04:13 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:02:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 10:03:31 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-26 10:00:11 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-26 10:02:01 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.011 |  |
| 2026-06-26 09:06:41 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.019 |  |
| 2026-06-26 10:04:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-26 10:11:08 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.035 |  |
| 2026-06-26 10:06:51 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.038 |  |
| 2026-06-26 10:04:36 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-06-26 10:08:04 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.048 |  |
| 2026-06-26 10:02:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.246 |  |
| 2026-06-26 10:06:31 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -58.852 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)