# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_07:09:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,646 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 07:09:14 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.136 |  |
| 2026-04-23 07:08:13 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:46 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.082 |  |
| 2026-04-23 07:07:35 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:33 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:04 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 07:07:01 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:06:46 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-23 07:06:42 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.146 |  |
| 2026-04-23 07:06:21 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 07:05:54 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-23 07:05:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-23 07:05:36 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:05:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 07:05:32 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-04-23 07:05:15 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:04:33 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:04:16 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 07:04:06 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-23 07:04:01 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 07:03:57 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:03:56 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:03:26 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-04-23 07:03:08 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:02:35 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-23 07:02:23 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-23 07:02:23 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-23 07:02:21 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.044 |  |
| 2026-04-23 07:02:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-04-23 07:02:14 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.079 |  |
| 2026-04-23 07:02:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:01:57 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:01:25 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.003 |  |
| 2026-04-23 07:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-23 07:01:08 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 07:00:40 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 06:30:20 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.018 |  |
| 2026-04-23 06:20:15 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.210 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 06:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 1.863 | 🔺 Rising |
| 2026-04-23 07:05:54 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-23 06:07:11 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-23 07:02:23 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-23 07:07:04 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 07:04:01 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 07:06:21 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 07:02:23 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-23 07:01:08 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 07:05:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 07:02:35 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-23 07:06:46 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-23 07:04:16 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 07:01:25 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.003 |  |
| 2026-04-23 07:01:57 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:35 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:02:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:03:57 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:05:15 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:01 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:07:33 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:08:13 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-23 07:03:08 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:05:36 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:03:56 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:00:40 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 07:04:06 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-23 07:05:32 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-04-23 07:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-23 07:03:26 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-04-23 07:02:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-04-23 07:02:21 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.044 |  |
| 2026-04-23 06:02:24 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.050 |  |
| 2026-04-23 06:05:20 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-04-23 07:05:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-23 07:02:14 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.079 |  |
| 2026-04-23 07:07:46 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.082 |  |
| 2026-04-23 07:09:14 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.136 |  |
| 2026-04-23 07:06:42 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)