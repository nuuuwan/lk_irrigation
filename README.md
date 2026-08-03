# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_04:04:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 04:04:37 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | -0.214 |  |
| 2026-08-04 04:04:37 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.023 |  |
| 2026-08-04 04:04:30 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-04 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.081 |  |
| 2026-08-04 04:04:28 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.075 |  |
| 2026-08-04 04:04:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-04 04:03:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:03:26 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-04 04:02:49 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 04:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:02:19 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.400 |  |
| 2026-08-04 04:02:16 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-04 04:02:07 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.610 |  |
| 2026-08-04 04:01:58 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 04:01:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-04 04:01:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:01:29 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-08-04 04:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:00:59 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.186 |  |
| 2026-08-04 03:21:56 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.039 |  |
| 2026-08-04 03:20:23 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-08-04 03:18:12 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 03:07:45 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.083 |  |
| 2026-08-04 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-08-04 04:04:37 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | -0.023 |  |
| 2026-08-04 03:09:51 | Glencourse (Kelani Ganga) | 15.81 | 🟡 Alert | -0.184 |  |
| 2026-08-04 04:04:37 | Peradeniya (Mahaweli Ganga) | 5.98 | 🟡 Alert | -0.214 |  |
| 2026-08-04 03:04:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-08-04 03:06:36 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-04 03:04:35 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-04 04:04:30 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-04 04:01:58 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 03:07:18 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 04:02:16 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-04 03:10:31 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-04 04:02:49 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 04:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:02:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:02 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:03:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:03 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:06:57 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 04:01:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-04 04:04:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-04 03:04:49 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-04 04:03:26 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-08-04 04:01:29 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2026-08-04 03:20:23 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-08-04 03:21:56 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.039 |  |
| 2026-08-04 03:03:19 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.042 |  |
| 2026-08-04 03:10:23 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | -0.049 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 04:04:28 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.075 |  |
| 2026-08-04 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.081 |  |
| 2026-08-04 04:00:59 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.186 |  |
| 2026-08-04 04:02:19 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.400 |  |
| 2026-08-04 04:02:07 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.610 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)