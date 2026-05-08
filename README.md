# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_19:20:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,436 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 19:20:04 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:18:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:17:32 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 19:17:18 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:15:42 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-08 19:15:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-05-08 19:13:59 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-08 19:10:33 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-08 19:10:09 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:10:07 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-08 19:08:26 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:07:52 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-08 19:07:50 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.046 |  |
| 2026-05-08 19:06:57 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:06:57 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-08 19:05:32 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-05-08 19:05:29 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-05-08 19:05:23 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-08 19:05:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:04:48 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 19:04:45 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.019 |  |
| 2026-05-08 19:04:41 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-08 19:04:40 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 19:04:09 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 19:03:16 | Kuda Oya (Kirindi Oya) | 4.35 | 🟢 Normal | 2.278 | 🔺 Rising |
| 2026-05-08 19:03:15 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-08 19:02:22 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.196 |  |
| 2026-05-08 19:02:18 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-05-08 19:02:12 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-08 19:01:59 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-05-08 19:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:01:32 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-08 19:01:22 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 19:01:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.064 |  |
| 2026-05-08 19:00:13 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.094 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 18:01:16 | Wellawaya (Kirindi Oya) | 5.35 | 🟡 Alert | 3.919 | 🔺 Rising |
| 2026-05-08 19:03:16 | Kuda Oya (Kirindi Oya) | 4.35 | 🟢 Normal | 2.278 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 19:05:32 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-05-08 19:01:59 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-05-08 19:10:33 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-08 19:06:57 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-08 19:05:29 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-05-08 19:03:15 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-08 19:05:23 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-08 18:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 19:13:59 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-08 19:00:13 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-08 19:10:07 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-08 19:15:42 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-08 19:07:52 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-08 19:02:12 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 19:04:48 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 19:01:22 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 19:04:09 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 19:04:40 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 19:17:32 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 19:05:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:08:26 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:10:09 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:20:04 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:02:22 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:06:57 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 19:15:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-05-08 19:01:32 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-08 19:04:41 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-08 19:04:45 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.019 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 19:07:50 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.046 |  |
| 2026-05-08 19:02:18 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-05-08 19:01:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.064 |  |
| 2026-05-08 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)