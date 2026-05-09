# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_08:17:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 08:17:21 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:13:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.017 |  |
| 2026-05-09 08:08:39 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 08:08:27 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.018 |  |
| 2026-05-09 08:07:58 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-09 08:07:14 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.075 |  |
| 2026-05-09 08:07:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-05-09 08:07:09 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.147 |  |
| 2026-05-09 08:06:58 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-05-09 08:06:51 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-05-09 08:06:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-05-09 08:06:09 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | -0.191 |  |
| 2026-05-09 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.067 |  |
| 2026-05-09 08:05:05 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.063 |  |
| 2026-05-09 08:05:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-09 08:04:59 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-05-09 08:04:17 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-09 08:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-05-09 08:03:59 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-09 08:03:46 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 08:03:23 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-05-09 08:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-05-09 08:03:18 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.032 |  |
| 2026-05-09 08:03:13 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2026-05-09 08:02:39 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.118 |  |
| 2026-05-09 08:02:26 | Galgamuwa (Mee Oya) | 2.85 | 🟢 Normal | -0.032 |  |
| 2026-05-09 08:02:05 | Kuda Oya (Kirindi Oya) | 2.97 | 🟢 Normal | -0.079 |  |
| 2026-05-09 08:01:50 | Thanthirimale (Malwathu Oya) | 3.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 08:01:43 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:01:39 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.097 |  |
| 2026-05-09 08:01:25 | Thanamalwila (Kirindi Oya) | 2.61 | 🟢 Normal | -0.393 |  |
| 2026-05-09 08:01:14 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2026-05-09 08:01:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:00:56 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-09 08:00:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.245 |  |
| 2026-05-09 08:00:20 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 08:03:23 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-05-09 05:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-09 08:00:56 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-09 08:07:58 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-09 08:03:59 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-09 08:01:50 | Thanthirimale (Malwathu Oya) | 3.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 08:03:46 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 08:08:39 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 08:05:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-09 08:01:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:17:21 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:01:43 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 08:06:58 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-05-09 08:13:10 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.017 |  |
| 2026-05-09 08:08:27 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.018 |  |
| 2026-05-09 08:06:51 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-05-09 08:03:13 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2026-05-09 07:10:09 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-05-09 08:07:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-05-09 08:00:20 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-05-09 08:04:17 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-09 08:02:26 | Galgamuwa (Mee Oya) | 2.85 | 🟢 Normal | -0.032 |  |
| 2026-05-09 08:03:18 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.032 |  |
| 2026-05-09 08:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-05-09 07:18:35 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.035 |  |
| 2026-05-09 08:01:14 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2026-05-09 08:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-05-09 08:04:59 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-05-09 08:05:05 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.063 |  |
| 2026-05-09 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.067 |  |
| 2026-05-09 08:06:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-05-09 08:07:14 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.075 |  |
| 2026-05-09 08:02:05 | Kuda Oya (Kirindi Oya) | 2.97 | 🟢 Normal | -0.079 |  |
| 2026-05-09 08:01:39 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.097 |  |
| 2026-05-09 08:02:39 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.118 |  |
| 2026-05-09 08:07:09 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.147 |  |
| 2026-05-09 08:06:09 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | -0.191 |  |
| 2026-05-09 08:00:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.245 |  |
| 2026-05-09 08:01:25 | Thanamalwila (Kirindi Oya) | 2.61 | 🟢 Normal | -0.393 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)