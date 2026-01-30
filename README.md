# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_13:19:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 13:19:10 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 13:17:56 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-30 13:16:19 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:14:55 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:11:24 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:10:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:09:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:08:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:08:01 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:07:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:07:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-30 13:06:12 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.131 |  |
| 2026-01-30 13:04:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:48 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.038 |  |
| 2026-01-30 13:04:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-30 13:04:30 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-30 13:04:19 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 13:04:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:01 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-30 13:03:54 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:03:29 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-30 13:03:19 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-30 13:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-01-30 13:02:25 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 13:02:19 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-01-30 13:01:51 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:45 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-30 13:01:43 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-30 13:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:26 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:23 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-30 13:00:25 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:00:22 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 13:01:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-30 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-30 13:04:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-30 13:01:43 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-30 13:19:10 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 13:02:25 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 13:07:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-30 13:04:19 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 13:03:19 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 13:01:51 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:26 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:01:23 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:02:19 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:10:26 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:16:19 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:30 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-30 12:07:44 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:14:55 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:03:54 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:08:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:04:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:00:25 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:07:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:09:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:11:24 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 13:17:56 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-30 13:03:29 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-30 13:04:01 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-30 13:01:45 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-30 13:00:22 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.014 |  |
| 2026-01-30 13:04:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-30 13:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-01-30 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-01-30 13:04:48 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.038 |  |
| 2026-01-30 13:06:12 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)