# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_20:09:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 20:09:24 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:07:58 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:07:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-28 20:07:06 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-28 20:07:01 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:06:11 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-06-28 20:05:53 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-28 20:05:43 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-06-28 20:05:06 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:05:00 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:04:36 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:04:36 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-28 20:04:29 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:04:23 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-28 20:04:10 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-28 20:04:02 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:03:56 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.053 |  |
| 2026-06-28 20:03:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-06-28 20:03:50 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:03:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:03:13 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-28 20:03:04 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:02:24 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:17 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-28 20:02:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:13 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:02:09 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-28 20:02:03 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:01:48 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:01:16 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:01:13 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:01:07 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:00:49 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:00:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 20:05:43 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-06-28 20:05:53 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-28 20:04:36 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-28 20:04:10 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-28 20:04:23 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-28 20:07:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-28 20:02:09 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-28 20:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-28 20:03:50 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:03:21 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:05:06 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 20:04:36 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:00:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:01:16 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:09:24 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:03 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:04:02 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:01:48 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:00:49 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:17 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:05:00 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:07:58 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:03:13 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:02:24 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 20:04:29 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:03:04 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:02:13 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:01:07 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:07:01 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:01:13 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-28 20:07:06 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-28 20:03:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-06-28 20:02:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-28 20:03:56 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.053 |  |
| 2026-06-28 20:06:11 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)