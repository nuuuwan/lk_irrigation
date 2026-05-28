# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_07:31:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 07:31:43 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:31:31 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:26:27 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | -0.072 |  |
| 2026-05-28 07:20:54 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.106 |  |
| 2026-05-28 07:18:48 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 07:14:46 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 07:11:08 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:08:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-05-28 07:07:17 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.054 |  |
| 2026-05-28 07:06:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:06:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:06:02 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-28 07:05:39 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.058 |  |
| 2026-05-28 07:05:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:04:35 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.019 |  |
| 2026-05-28 07:04:23 | Glencourse (Kelani Ganga) | 11.95 | 🟢 Normal | -0.128 |  |
| 2026-05-28 07:04:21 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | -0.043 |  |
| 2026-05-28 07:04:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-05-28 07:03:44 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.069 |  |
| 2026-05-28 07:03:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-05-28 07:03:30 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:03:11 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-28 07:03:04 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:47 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:43 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:22 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:16 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:12 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-28 07:02:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:01:55 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.023 |  |
| 2026-05-28 07:01:55 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.043 |  |
| 2026-05-28 07:01:48 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.049 |  |
| 2026-05-28 07:01:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-28 07:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:01:08 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:00:41 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-28 07:00:40 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 07:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 07:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-05-28 07:01:48 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.049 |  |
| 2026-05-28 07:01:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-28 07:14:46 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 07:00:40 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 07:18:48 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 07:03:30 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:01:08 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:05:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:04:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 07:00:41 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-28 07:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:11:08 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:43 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:03:04 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:31:43 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:16 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:31:31 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:06:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:47 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:06:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:02:22 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 07:06:02 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-28 07:02:12 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-28 07:03:11 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-28 07:08:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-05-28 07:04:35 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.019 |  |
| 2026-05-28 07:01:55 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.023 |  |
| 2026-05-28 07:03:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-05-28 07:04:21 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | -0.043 |  |
| 2026-05-28 07:01:55 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.043 |  |
| 2026-05-28 07:07:17 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.054 |  |
| 2026-05-28 07:05:39 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.058 |  |
| 2026-05-28 07:03:44 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.069 |  |
| 2026-05-28 07:26:27 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | -0.072 |  |
| 2026-05-28 07:20:54 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.106 |  |
| 2026-05-28 07:04:23 | Glencourse (Kelani Ganga) | 11.95 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)