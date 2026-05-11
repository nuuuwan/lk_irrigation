# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_08:23:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,715 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 08:23:16 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 08:20:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:17:36 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-11 08:08:49 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.094 |  |
| 2026-05-11 08:07:54 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.167 |  |
| 2026-05-11 08:07:33 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 08:07:25 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-11 08:06:35 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.029 |  |
| 2026-05-11 08:06:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:06:32 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 08:06:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.009 |  |
| 2026-05-11 08:05:46 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-11 08:05:41 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 08:05:37 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 08:05:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:05:18 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.051 |  |
| 2026-05-11 08:04:52 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-11 08:04:44 | Thanamalwila (Kirindi Oya) | 3.09 | 🟢 Normal | -0.323 |  |
| 2026-05-11 08:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.056 |  |
| 2026-05-11 08:04:28 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.033 |  |
| 2026-05-11 08:04:17 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:04:10 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 08:03:38 | Kuda Oya (Kirindi Oya) | 3.21 | 🟢 Normal | -0.260 |  |
| 2026-05-11 08:03:28 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 08:03:05 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-11 08:02:51 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-05-11 08:02:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.054 |  |
| 2026-05-11 08:02:10 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 08:02:03 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:01:59 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:01:46 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-11 08:01:42 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:01:27 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-11 08:01:18 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:00:55 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:00:25 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:00:23 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 08:07:25 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-11 08:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-11 08:23:16 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 08:06:32 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 08:01:27 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-11 08:05:37 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 08:07:33 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 08:01:46 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-11 08:03:05 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-11 08:05:46 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-11 08:03:28 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-11 08:04:10 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 07:37:33 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 08:02:10 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 08:17:36 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:01:18 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:01:42 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:06:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:00:25 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:00:55 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:20:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 08:06:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.009 |  |
| 2026-05-11 08:02:03 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:05:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:01:59 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:04:17 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:00:23 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-11 08:02:51 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-05-11 08:04:52 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-11 08:05:41 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 08:06:35 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.029 |  |
| 2026-05-11 08:04:28 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.033 |  |
| 2026-05-11 08:05:18 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.051 |  |
| 2026-05-11 08:02:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.054 |  |
| 2026-05-11 08:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.056 |  |
| 2026-05-11 08:08:49 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.094 |  |
| 2026-05-11 08:07:54 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.167 |  |
| 2026-05-11 08:03:38 | Kuda Oya (Kirindi Oya) | 3.21 | 🟢 Normal | -0.260 |  |
| 2026-05-11 08:04:44 | Thanamalwila (Kirindi Oya) | 3.09 | 🟢 Normal | -0.323 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)