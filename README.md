# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_07:23:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 07:23:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 07:22:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.022 |  |
| 2026-05-08 07:17:41 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.032 |  |
| 2026-05-08 07:09:54 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.130 |  |
| 2026-05-08 07:07:38 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-08 07:07:19 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.105 |  |
| 2026-05-08 07:07:11 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.245 |  |
| 2026-05-08 07:06:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:06:32 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.045 |  |
| 2026-05-08 07:05:55 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-08 07:05:46 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.308 |  |
| 2026-05-08 07:05:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-05-08 07:05:22 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-08 07:05:20 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-08 07:05:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-05-08 07:04:47 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 07:04:21 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.153 |  |
| 2026-05-08 07:04:18 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:04:16 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-05-08 07:03:57 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.068 |  |
| 2026-05-08 07:03:53 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | -0.170 |  |
| 2026-05-08 07:03:39 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-08 07:03:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-08 07:03:01 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.052 |  |
| 2026-05-08 07:03:00 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.056 |  |
| 2026-05-08 07:02:56 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:02:40 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-05-08 07:02:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:01:48 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-08 07:01:48 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 07:01:42 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-08 07:01:42 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.965 | 🔺 Rising |
| 2026-05-08 07:01:22 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-05-08 07:01:22 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-08 07:01:21 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-05-08 07:01:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-05-08 07:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 07:00:38 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.023 |  |
| 2026-05-08 06:42:33 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 07:01:42 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.965 | 🔺 Rising |
| 2026-05-08 07:03:39 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-08 07:05:22 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-08 07:05:20 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-08 07:01:22 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-08 07:01:48 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-08 07:05:55 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-08 07:07:38 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-08 07:01:48 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 07:23:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 07:01:42 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-08 07:03:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-08 07:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 07:04:47 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 07:06:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:02:56 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:04:18 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:02:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-08 07:02:40 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-05-08 07:05:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-05-08 07:04:16 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-05-08 07:01:21 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-05-08 07:22:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.022 |  |
| 2026-05-08 07:00:38 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.023 |  |
| 2026-05-08 07:01:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-05-08 07:17:41 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.032 |  |
| 2026-05-08 07:05:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-05-08 07:06:32 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.045 |  |
| 2026-05-08 07:03:01 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.052 |  |
| 2026-05-08 07:03:00 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.056 |  |
| 2026-05-08 06:04:16 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.062 |  |
| 2026-05-08 07:03:57 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.068 |  |
| 2026-05-08 07:07:19 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.105 |  |
| 2026-05-08 07:01:22 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-05-08 07:09:54 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.130 |  |
| 2026-05-08 07:04:21 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.153 |  |
| 2026-05-08 07:03:53 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | -0.170 |  |
| 2026-05-08 07:07:11 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.245 |  |
| 2026-05-08 07:05:46 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.308 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)