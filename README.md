# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_07:18:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 07:18:15 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:13:17 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-04-09 07:10:20 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:07:37 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-09 07:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 07:06:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-09 07:06:43 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.019 |  |
| 2026-04-09 07:06:32 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:06:07 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-04-09 07:05:45 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.177 |  |
| 2026-04-09 07:05:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:05:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:04:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-09 07:04:18 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-09 07:04:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-09 07:03:55 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-04-09 07:03:41 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:03:30 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-04-09 07:03:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:03:23 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 07:03:04 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-09 07:02:58 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-04-09 07:02:53 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:02:37 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:02:15 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 07:02:12 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:40 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:16 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 1.414 | 🔺 Rising |
| 2026-04-09 07:01:12 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:05 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-04-09 07:00:53 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-09 07:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 06:41:06 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 07:01:16 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 1.414 | 🔺 Rising |
| 2026-04-09 07:00:53 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-09 07:04:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-09 06:10:03 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-09 07:03:04 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-09 07:07:37 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-09 07:06:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-09 07:03:23 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 07:04:18 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-09 07:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 07:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 07:02:15 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 07:02:37 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:40 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:02:12 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:02:53 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:18:15 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:05:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:05:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:12 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:10:20 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:03:55 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:03:41 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:06:32 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:03:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-09 07:02:58 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-04-09 06:10:28 | Panadugama (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-04-09 07:06:43 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.019 |  |
| 2026-04-09 07:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-04-09 06:06:36 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-09 07:01:05 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-04-09 07:06:07 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-04-09 07:13:17 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-04-09 07:03:30 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-04-09 07:04:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-09 07:05:45 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)