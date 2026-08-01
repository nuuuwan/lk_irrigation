# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_22:21:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 22:21:53 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.055 |  |
| 2026-08-01 22:17:02 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.008 |  |
| 2026-08-01 22:14:41 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 22:14:05 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.173 |  |
| 2026-08-01 22:13:43 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-08-01 22:12:38 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.036 |  |
| 2026-08-01 22:11:18 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-08-01 22:09:00 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.035 |  |
| 2026-08-01 22:09:00 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.330 |  |
| 2026-08-01 22:08:48 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:07:47 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.018 |  |
| 2026-08-01 22:06:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-08-01 22:06:27 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.160 |  |
| 2026-08-01 22:06:17 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.094 |  |
| 2026-08-01 22:05:23 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:05:00 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-08-01 22:04:27 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:04:20 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-08-01 22:04:06 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:03:55 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-01 22:03:51 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:03:42 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:03:38 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.138 |  |
| 2026-08-01 22:03:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:02:26 | Hanwella (Kelani Ganga) | 4.91 | 🟢 Normal | -0.209 |  |
| 2026-08-01 22:02:08 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:01:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:18 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:10 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.083 |  |
| 2026-08-01 22:00:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:00:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 22:14:41 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 22:03:51 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:05:23 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 22:02:08 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:18 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:00:40 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:08:48 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:04:06 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:00:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:01:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:03:07 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:03:42 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:04:27 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 22:17:02 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.008 |  |
| 2026-08-01 22:13:43 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-08-01 22:06:28 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-08-01 22:03:55 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-01 22:11:18 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-08-01 22:07:47 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.018 |  |
| 2026-08-01 22:04:20 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-08-01 22:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-08-01 22:09:00 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.035 |  |
| 2026-08-01 22:12:38 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.036 |  |
| 2026-08-01 22:05:00 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 22:21:53 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.055 |  |
| 2026-08-01 22:01:10 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.083 |  |
| 2026-08-01 22:06:17 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.094 |  |
| 2026-08-01 22:03:38 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.138 |  |
| 2026-08-01 22:06:27 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.160 |  |
| 2026-08-01 22:14:05 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.173 |  |
| 2026-08-01 22:02:26 | Hanwella (Kelani Ganga) | 4.91 | 🟢 Normal | -0.209 |  |
| 2026-08-01 22:09:00 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | -0.330 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)