# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_15:29:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 15:29:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:18:04 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:12:56 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-07-05 15:11:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:10:33 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-07-05 15:09:26 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-07-05 15:08:37 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:08:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-05 15:07:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:06:37 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:06:23 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:05:20 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:05:06 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.039 |  |
| 2026-07-05 15:04:49 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-07-05 15:04:46 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.128 |  |
| 2026-07-05 15:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.100 |  |
| 2026-07-05 15:04:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:04:10 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:03:49 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:03:40 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.080 |  |
| 2026-07-05 15:03:35 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:03:21 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:03:13 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-05 15:02:53 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.089 |  |
| 2026-07-05 15:02:41 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 15:02:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-05 15:01:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:01:26 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:01:25 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:01:17 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:01:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:01:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.013 |  |
| 2026-07-05 15:01:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:59 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:22 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 14:59:46 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 15:08:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-05 15:02:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-05 15:02:41 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 15:00:22 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:04:10 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:29:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:01:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:01:17 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:00:59 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:07:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:03:49 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:11:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:06:37 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:08:37 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:01:26 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:18:04 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:05:20 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:04:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:06:23 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:12:56 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-07-05 15:09:26 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-07-05 15:01:25 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:03:35 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:01:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-07-05 15:03:13 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-05 15:01:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.013 |  |
| 2026-07-05 15:10:33 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-07-05 15:03:21 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:03:20 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:01:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2026-07-05 15:05:06 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.039 |  |
| 2026-07-05 15:04:49 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-07-05 15:03:40 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.080 |  |
| 2026-07-05 15:02:53 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.089 |  |
| 2026-07-05 15:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.100 |  |
| 2026-07-05 15:04:46 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)