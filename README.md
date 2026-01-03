# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_14:19:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,567 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 14:19:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:16:51 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.016 |  |
| 2026-01-03 14:11:10 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:10:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 14:08:44 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:07:57 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:07:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:06:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-03 14:06:23 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-03 14:05:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:05:26 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-03 14:05:16 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.030 |  |
| 2026-01-03 14:05:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:04:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:04:25 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.030 |  |
| 2026-01-03 14:04:16 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:04:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 14:03:28 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:03:25 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:03:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:02:50 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:02:37 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:02:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-03 14:02:24 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:02:15 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:02:09 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:01:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-01-03 14:01:50 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:46 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:40 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:27 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:01:10 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:01:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.041 |  |
| 2026-01-03 14:01:09 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:00:47 | Galgamuwa (Mee Oya) | 2.58 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:00:27 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:00:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 14:06:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-03 14:05:26 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-03 14:02:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-03 14:10:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 14:04:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 14:01:09 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:00:27 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:40 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:46 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:01:50 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:19:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:07:57 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:02:50 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:03:28 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:02:37 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:08:44 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:03:06 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:05:33 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:04:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:05:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:07:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:11:10 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-03 14:06:23 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-01-03 14:01:27 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:01:10 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:02:09 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:02:24 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:03:25 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:02:15 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:16:51 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.016 |  |
| 2026-01-03 14:04:16 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:00:47 | Galgamuwa (Mee Oya) | 2.58 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:00:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:05:16 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.030 |  |
| 2026-01-03 14:04:25 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.030 |  |
| 2026-01-03 14:01:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.041 |  |
| 2026-01-03 14:01:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)