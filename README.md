# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_00:18:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 00:18:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-05-12 00:16:35 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-05-12 00:16:04 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:12:54 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:12:37 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:10:54 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-05-12 00:10:35 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:08:39 | Kuda Oya (Kirindi Oya) | 2.58 | 🟢 Normal | -0.019 |  |
| 2026-05-12 00:07:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 00:06:57 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:53 | Moragaswewa (Deduru Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-12 00:06:18 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:13 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:09 | Moragaswewa (Deduru Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:05:25 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 00:05:20 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 00:05:09 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-12 00:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 00:04:43 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:04:38 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 00:04:32 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 00:04:11 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.142 |  |
| 2026-05-12 00:04:11 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-05-12 00:04:01 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-05-12 00:03:51 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 00:03:34 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 00:03:03 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.080 |  |
| 2026-05-12 00:02:52 | Siyambalanduwa (Heda Oya) | 1.83 | 🟢 Normal | -0.321 |  |
| 2026-05-12 00:02:47 | Thanamalwila (Kirindi Oya) | 2.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-12 00:02:32 | Katharagama (Menik Ganga) | 2.25 | 🟢 Normal | -0.042 |  |
| 2026-05-12 00:02:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-05-12 00:02:21 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 00:01:52 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 00:01:39 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-05-12 00:01:06 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:00:30 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -11.520 |  |
| 2026-05-12 00:00:26 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.097 |  |
| 2026-05-12 00:00:05 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -11.520 |  |
| 2026-05-11 23:50:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.154 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 00:16:35 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-05-12 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-12 00:05:09 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 00:01:52 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 00:02:47 | Thanamalwila (Kirindi Oya) | 2.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-12 00:03:51 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 00:04:32 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 00:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 00:04:38 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 00:02:21 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 00:05:20 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 00:03:34 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 00:05:25 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 00:06:53 | Moragaswewa (Deduru Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:04:43 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:13 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:12:54 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:16:04 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:18 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:01:06 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:12:37 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:57 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:18:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-05-12 00:08:39 | Kuda Oya (Kirindi Oya) | 2.58 | 🟢 Normal | -0.019 |  |
| 2026-05-12 00:02:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-05-12 00:01:39 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-05-12 00:04:01 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-05-12 00:04:11 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-05-12 00:10:54 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-05-12 00:07:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 00:02:32 | Katharagama (Menik Ganga) | 2.25 | 🟢 Normal | -0.042 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-12 00:03:03 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.080 |  |
| 2026-05-12 00:00:26 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.097 |  |
| 2026-05-12 00:04:11 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.142 |  |
| 2026-05-12 00:02:52 | Siyambalanduwa (Heda Oya) | 1.83 | 🟢 Normal | -0.321 |  |
| 2026-05-12 00:00:30 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -11.520 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)