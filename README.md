# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_20:26:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 20:26:46 | Wellawaya (Kirindi Oya) | 4.63 | 🟡 Alert | -0.297 |  |
| 2026-05-08 20:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 20:13:31 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 20:11:00 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:09:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:08:34 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:07:29 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.050 |  |
| 2026-05-08 20:07:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.048 |  |
| 2026-05-08 20:06:12 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-05-08 20:05:41 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-08 20:05:30 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:05:29 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-08 20:05:23 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:05:19 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:04:26 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 20:04:26 | Moragaswewa (Deduru Oya) | 1.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-08 20:04:19 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:04:06 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-08 20:04:04 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:03:53 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 20:03:23 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.058 |  |
| 2026-05-08 20:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.108 |  |
| 2026-05-08 20:03:10 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-05-08 20:03:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-05-08 20:03:01 | Thanamalwila (Kirindi Oya) | 3.48 | 🟢 Normal | 1.336 | 🔺 Rising |
| 2026-05-08 20:03:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:02:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-05-08 20:02:43 | Magura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-05-08 20:02:37 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 20:02:22 | Kuda Oya (Kirindi Oya) | 5.35 | 🟢 Normal | 1.015 | 🔺 Rising |
| 2026-05-08 20:02:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:02:08 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:02:07 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-08 20:01:31 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:01:26 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:01:07 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-08 20:01:05 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 20:26:46 | Wellawaya (Kirindi Oya) | 4.63 | 🟡 Alert | -0.297 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 20:03:01 | Thanamalwila (Kirindi Oya) | 3.48 | 🟢 Normal | 1.336 | 🔺 Rising |
| 2026-05-08 20:02:22 | Kuda Oya (Kirindi Oya) | 5.35 | 🟢 Normal | 1.015 | 🔺 Rising |
| 2026-05-08 20:06:12 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-05-08 20:02:43 | Magura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-05-08 20:02:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-05-08 20:04:06 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-08 20:01:07 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-08 20:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 20:04:26 | Moragaswewa (Deduru Oya) | 1.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-08 20:02:07 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-08 20:03:53 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 20:04:26 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 20:05:41 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 20:02:37 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 20:13:31 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 20:05:29 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-08 20:11:00 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:02:08 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:03:00 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:04:19 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:02:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:09:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:08:34 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:01:05 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:04:04 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:01:31 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 20:05:30 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:05:23 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:05:19 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-08 20:03:10 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 20:07:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.048 |  |
| 2026-05-08 20:07:29 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.050 |  |
| 2026-05-08 20:03:23 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.058 |  |
| 2026-05-08 20:03:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-05-08 20:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)