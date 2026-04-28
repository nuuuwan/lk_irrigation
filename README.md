# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_06:32:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 06:32:56 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 06:13:06 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-28 06:13:02 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-04-28 06:12:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:10:59 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-28 06:10:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:09:37 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.100 |  |
| 2026-04-28 06:07:05 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-28 06:06:22 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-04-28 06:06:19 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.019 |  |
| 2026-04-28 06:05:12 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.108 |  |
| 2026-04-28 06:04:45 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:04:34 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 06:04:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:03:56 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-04-28 06:03:50 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:03:48 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:03:19 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:02:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:02:53 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-04-28 06:02:43 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.050 |  |
| 2026-04-28 06:02:43 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-04-28 06:02:33 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.033 |  |
| 2026-04-28 06:02:26 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.053 |  |
| 2026-04-28 06:02:25 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:02:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:02:10 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 06:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.340 |  |
| 2026-04-28 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-28 06:01:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:01:43 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.025 |  |
| 2026-04-28 06:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 06:01:22 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-04-28 06:01:19 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-28 06:01:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-04-28 06:00:39 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-28 06:00:36 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.080 |  |
| 2026-04-28 05:47:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.340 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 06:10:59 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-28 06:13:06 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-28 06:00:39 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-28 05:09:39 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-28 06:07:05 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-28 06:01:19 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-28 06:04:34 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-28 06:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 06:02:10 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 06:32:56 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 06:10:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:01:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:02:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:12:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:03:50 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:01:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:03:19 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:04:45 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 06:02:25 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:02:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:04:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-28 06:06:19 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.019 |  |
| 2026-04-28 06:01:22 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-04-28 06:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-04-28 06:01:43 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.025 |  |
| 2026-04-28 06:13:02 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-04-28 06:06:22 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-04-28 06:02:53 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-04-28 06:03:56 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-04-28 06:02:33 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.033 |  |
| 2026-04-28 06:02:43 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.050 |  |
| 2026-04-28 06:02:26 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.053 |  |
| 2026-04-28 06:02:43 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-04-28 06:00:36 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.080 |  |
| 2026-04-28 06:09:37 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.100 |  |
| 2026-04-28 06:05:12 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.108 |  |
| 2026-04-28 06:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.340 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)