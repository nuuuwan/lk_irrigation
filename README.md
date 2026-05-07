# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_05:28:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 05:28:45 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.140 |  |
| 2026-05-07 05:26:24 | Horowpothana (Yan Oya) | 2.88 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-07 05:15:43 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.074 |  |
| 2026-05-07 05:11:44 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-05-07 05:08:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-07 05:06:17 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-07 05:06:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-07 05:05:55 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-07 05:05:53 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -18.000 |  |
| 2026-05-07 05:05:46 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-05-07 05:05:43 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -18.000 |  |
| 2026-05-07 05:04:49 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.057 |  |
| 2026-05-07 05:04:45 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 05:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:03:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:03:53 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-07 05:03:37 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-07 05:03:24 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-07 05:03:03 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-07 05:02:50 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.005 |  |
| 2026-05-07 05:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.068 |  |
| 2026-05-07 05:01:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:52 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.066 |  |
| 2026-05-07 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-07 05:01:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-07 05:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 05:01:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-07 05:01:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-07 05:00:53 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 05:00:44 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.093 |  |
| 2026-05-07 05:00:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 05:05:55 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-07 05:11:44 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-05-07 05:03:24 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-07 04:03:13 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 05:03:53 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-07 05:26:24 | Horowpothana (Yan Oya) | 2.88 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-07 05:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 05:06:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-07 05:06:17 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-07 05:01:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-07 05:03:37 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-07 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-07 05:01:05 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:01:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 05:08:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-07 05:00:53 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 05:04:45 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 05:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:03:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:00:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:01:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:02:50 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.005 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 05:03:03 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-07 05:05:46 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-05-07 05:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-07 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-07 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-07 05:04:49 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.057 |  |
| 2026-05-07 05:01:52 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.066 |  |
| 2026-05-07 05:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.068 |  |
| 2026-05-07 05:15:43 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.074 |  |
| 2026-05-07 05:00:44 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.093 |  |
| 2026-05-07 05:28:45 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.140 |  |
| 2026-05-07 05:05:53 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)