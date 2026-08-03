# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_05:06:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,386 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 05:06:13 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.013 |  |
| 2026-08-04 05:05:44 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.317 |  |
| 2026-08-04 05:05:23 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-08-04 05:05:19 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.180 |  |
| 2026-08-04 05:05:13 | Hanwella (Kelani Ganga) | 7.11 | 🟡 Alert | -0.040 |  |
| 2026-08-04 05:04:44 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:04:05 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:04:04 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-04 05:03:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:03:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 05:02:55 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.099 |  |
| 2026-08-04 05:02:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:02:48 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-08-04 05:02:43 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-08-04 05:02:31 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:44 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:37 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.324 |  |
| 2026-08-04 05:01:25 | Peradeniya (Mahaweli Ganga) | 5.62 | 🟡 Alert | -0.380 |  |
| 2026-08-04 05:01:25 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:15 | Ellagawa (Kalu Ganga) | 8.43 | 🟢 Normal | -0.021 |  |
| 2026-08-04 05:01:07 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:02 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-08-04 05:00:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:37:19 | Rathnapura (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.087 |  |
| 2026-08-04 04:34:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.023 |  |
| 2026-08-04 04:34:22 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-08-04 04:20:38 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.013 |  |
| 2026-08-04 04:18:37 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.180 |  |
| 2026-08-04 04:18:36 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.180 |  |
| 2026-08-04 04:18:35 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.180 |  |
| 2026-08-04 04:18:34 | Magura (Kalu Ganga) | 3.17 | 🟢 Normal | -0.180 |  |
| 2026-08-04 04:18:32 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.180 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 04:37:19 | Rathnapura (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.087 |  |
| 2026-08-04 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-08-04 05:05:13 | Hanwella (Kelani Ganga) | 7.11 | 🟡 Alert | -0.040 |  |
| 2026-08-04 05:01:25 | Peradeniya (Mahaweli Ganga) | 5.62 | 🟡 Alert | -0.380 |  |
| 2026-08-04 04:06:36 | Glencourse (Kelani Ganga) | 15.41 | 🟡 Alert | -0.423 |  |
| 2026-08-04 05:04:04 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-04 04:06:18 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-04 03:07:18 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 05:03:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 04:02:49 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 04:05:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 05:01:07 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:44 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:04:05 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:03:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:02:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:00:07 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:02:31 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:01:25 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:04:44 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 05:06:13 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.013 |  |
| 2026-08-04 04:34:22 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.014 |  |
| 2026-08-04 05:02:48 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-08-04 05:01:15 | Ellagawa (Kalu Ganga) | 8.43 | 🟢 Normal | -0.021 |  |
| 2026-08-04 05:01:02 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-08-04 05:05:23 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-08-04 05:02:43 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 04:04:28 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.075 |  |
| 2026-08-04 04:11:29 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-08-04 04:13:25 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.094 |  |
| 2026-08-04 05:02:55 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.099 |  |
| 2026-08-04 05:05:19 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.180 |  |
| 2026-08-04 04:00:59 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.186 |  |
| 2026-08-04 05:05:44 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.317 |  |
| 2026-08-04 05:01:37 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)