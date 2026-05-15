# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_20:22:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 20:22:49 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:19:15 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-05-15 20:12:31 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:11:34 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.038 |  |
| 2026-05-15 20:08:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:07:56 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-15 20:07:43 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.019 |  |
| 2026-05-15 20:06:12 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:05:36 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:05:36 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:05:29 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.043 |  |
| 2026-05-15 20:05:08 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-15 20:04:58 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-15 20:04:37 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 20:04:16 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-15 20:04:01 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:04:00 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.140 |  |
| 2026-05-15 20:03:52 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.074 |  |
| 2026-05-15 20:03:39 | Hanwella (Kelani Ganga) | 4.87 | 🟢 Normal | -0.114 |  |
| 2026-05-15 20:03:26 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:03:15 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-15 20:02:29 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:19 | Dunamale (Aththanagalu Oya) | 4.66 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 20:02:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:03 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:02:03 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:01 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.049 |  |
| 2026-05-15 20:01:42 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:40 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:38 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:19 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-15 20:01:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:00:56 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-15 20:00:46 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.049 |  |
| 2026-05-15 20:00:21 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 20:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 20:02:19 | Dunamale (Aththanagalu Oya) | 4.66 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 20:02:01 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.049 |  |
| 2026-05-15 20:01:19 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-15 20:00:56 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-15 20:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-15 20:03:15 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:05:36 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:22:49 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:42 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:40 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:04:16 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:01:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:12:31 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:02:03 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:05:36 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:08:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 20:07:56 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-15 20:04:37 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:04:01 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:06:12 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:03 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:02:29 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:03:26 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-15 20:05:08 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-15 20:07:43 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.019 |  |
| 2026-05-15 20:04:58 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-15 20:19:15 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-05-15 20:00:21 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-05-15 20:11:34 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.038 |  |
| 2026-05-15 20:05:29 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.043 |  |
| 2026-05-15 20:00:46 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.049 |  |
| 2026-05-15 20:03:52 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.074 |  |
| 2026-05-15 20:03:39 | Hanwella (Kelani Ganga) | 4.87 | 🟢 Normal | -0.114 |  |
| 2026-05-15 20:04:00 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)