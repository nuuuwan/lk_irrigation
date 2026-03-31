# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_04:48:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 04:48:25 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.006 |  |
| 2026-04-01 04:34:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:33:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:33:02 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:25:09 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:24:43 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:24:19 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-01 04:20:17 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:09:39 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:08:28 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:07:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.569 | 🔺 Rising |
| 2026-04-01 04:07:11 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:06:39 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:06:34 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:06:11 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.065 |  |
| 2026-04-01 04:05:46 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:05:32 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-04-01 04:04:35 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:04:30 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:04:24 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-01 04:04:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:03:09 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:50 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:48 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-01 04:01:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:07 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:41 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-04-01 04:00:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-04-01 04:07:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.569 | 🔺 Rising |
| 2026-04-01 01:07:34 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-01 04:01:48 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-01 04:24:19 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-01 01:04:29 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-01 01:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 04:07:11 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:04:35 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:06:39 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 04:05:46 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:24:43 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:50 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:04:30 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:25:09 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:06:11 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:09:39 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 02:06:26 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:41 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 03:07:22 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:03:09 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:33:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:00:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:04:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:01:07 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:06:34 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:34:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 03:01:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:20:17 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 04:48:25 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.006 |  |
| 2026-04-01 03:07:49 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-01 04:04:24 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-01 04:05:32 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-04-01 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.065 |  |
| 2026-03-31 18:01:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)