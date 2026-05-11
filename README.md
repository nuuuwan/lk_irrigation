# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_01:27:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 01:27:13 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.017 |  |
| 2026-05-12 01:18:23 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 01:15:13 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-12 01:13:33 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:08:58 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:06:06 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:06:03 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.076 |  |
| 2026-05-12 01:05:56 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-05-12 01:05:55 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.119 |  |
| 2026-05-12 01:05:48 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-05-12 01:05:33 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 01:05:12 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 01:04:49 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.059 |  |
| 2026-05-12 01:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 01:04:23 | Katharagama (Menik Ganga) | 2.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 01:04:07 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 01:03:51 | Siyambalanduwa (Heda Oya) | 1.56 | 🟢 Normal | -0.266 |  |
| 2026-05-12 01:02:58 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-05-12 01:02:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:02:49 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-12 01:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-12 01:02:28 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-12 01:02:25 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-12 01:02:21 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:02:15 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 01:01:30 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 01:01:29 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2026-05-12 01:01:16 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-05-12 01:01:11 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-12 01:15:13 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 01:01:30 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 01:04:07 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 01:02:49 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-12 01:05:33 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 01:04:23 | Katharagama (Menik Ganga) | 2.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 01:01:11 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 01:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 01:02:15 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 01:18:23 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 01:05:12 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 01:06:06 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:08:58 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:12:54 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:02:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:13:33 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:02:21 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-12 00:06:57 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:02:28 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-12 01:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-12 01:27:13 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.017 |  |
| 2026-05-12 00:08:39 | Kuda Oya (Kirindi Oya) | 2.58 | 🟢 Normal | -0.019 |  |
| 2026-05-12 01:02:25 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-12 01:02:58 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-05-12 00:04:01 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-05-12 01:01:16 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-05-12 00:07:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 01:05:56 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 01:01:29 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2026-05-12 01:05:48 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-05-12 01:04:49 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.059 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-12 01:06:03 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.076 |  |
| 2026-05-12 01:05:55 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.119 |  |
| 2026-05-12 01:03:51 | Siyambalanduwa (Heda Oya) | 1.56 | 🟢 Normal | -0.266 |  |
| 2026-05-12 00:00:30 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -11.520 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)