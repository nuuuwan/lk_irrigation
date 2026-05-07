# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_17:21:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 17:21:25 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.082 |  |
| 2026-05-07 17:12:59 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-07 17:11:38 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-07 17:11:01 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.053 |  |
| 2026-05-07 17:09:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:08:41 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:08:21 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-07 17:07:54 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:06:34 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.069 |  |
| 2026-05-07 17:06:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-05-07 17:06:18 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-07 17:05:58 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:05:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.089 |  |
| 2026-05-07 17:05:43 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 17:05:21 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-07 17:05:12 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-07 17:04:49 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-05-07 17:04:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:04:02 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-05-07 17:03:56 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.128 |  |
| 2026-05-07 17:03:41 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:03:23 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.048 |  |
| 2026-05-07 17:03:04 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-07 17:02:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-05-07 17:02:38 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.022 |  |
| 2026-05-07 17:02:34 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.042 |  |
| 2026-05-07 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:02:13 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-07 17:02:11 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 17:02:05 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-05-07 17:01:27 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:01:26 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:00:49 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:00:41 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:00:24 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:00:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.034 |  |
| 2026-05-07 17:00:07 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:59:31 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 17:04:49 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-05-07 17:02:13 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-05-07 17:02:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-05-07 17:03:04 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-07 17:11:38 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-07 16:04:56 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-07 17:08:21 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-07 17:06:18 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-07 17:05:21 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-07 17:02:38 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 17:05:12 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-07 17:02:11 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 17:12:59 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-07 17:05:43 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 17:00:07 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:01:27 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:05:58 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:09:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:00:24 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:04:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:01:26 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:08:41 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 17:06:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-05-07 17:07:54 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:00:49 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:03:41 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:00:41 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-07 17:04:02 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-05-07 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.022 |  |
| 2026-05-07 17:02:05 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-05-07 17:00:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.034 |  |
| 2026-05-07 17:02:34 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.042 |  |
| 2026-05-07 17:03:23 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.048 |  |
| 2026-05-07 17:11:01 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.053 |  |
| 2026-05-07 17:06:34 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.069 |  |
| 2026-05-07 17:21:25 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.082 |  |
| 2026-05-07 17:05:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.089 |  |
| 2026-05-07 17:03:56 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)