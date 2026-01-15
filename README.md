# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_19:16:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 19:16:39 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-01-15 19:13:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:12:09 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:09:29 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:06:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-01-15 19:06:58 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-15 19:06:46 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:06:39 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:06:21 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.056 |  |
| 2026-01-15 19:06:08 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 19:05:31 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-15 19:05:25 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:05:14 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:05:06 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-15 19:04:49 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-01-15 19:04:41 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-15 19:04:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:04:28 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 19:04:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 19:03:59 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-15 19:03:48 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:40 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:23 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:18 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.033 |  |
| 2026-01-15 19:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.058 |  |
| 2026-01-15 19:03:02 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:31 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:17 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.076 |  |
| 2026-01-15 19:02:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:01:49 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 18:02:12 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-15 19:05:06 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-15 19:03:59 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-15 19:04:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 19:05:31 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-15 19:04:28 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 19:06:08 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 19:06:58 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-15 19:01:49 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:12:09 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:31 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:02 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:48 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:05:25 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:40 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:38 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:03:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:13:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:06:46 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:04:39 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:09:29 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:06:39 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:05:14 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:02:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 19:04:49 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-01-15 19:04:41 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:00:27 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:07:03 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-01-15 19:06:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-01-15 19:03:18 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.033 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-15 19:16:39 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-01-15 19:06:21 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.056 |  |
| 2026-01-15 19:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.058 |  |
| 2026-01-15 19:02:17 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.076 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)