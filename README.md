# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_22:36:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,155 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 22:36:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 22:11:12 | Magura (Kalu Ganga) | 3.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-03 22:10:09 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-03 22:08:30 | Hanwella (Kelani Ganga) | 6.77 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-08-03 22:08:02 | Rathnapura (Kalu Ganga) | 8.07 | 🟠 Minor Flood | -0.089 |  |
| 2026-08-03 22:07:53 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-08-03 22:07:05 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.072 |  |
| 2026-08-03 22:06:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 22:06:31 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.058 |  |
| 2026-08-03 22:06:05 | Norwood (Kelani Ganga) | 1.71 | 🟡 Alert | -0.237 |  |
| 2026-08-03 22:05:29 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.333 |  |
| 2026-08-03 22:05:26 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-03 22:05:21 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:05:07 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-03 22:04:57 | Glencourse (Kelani Ganga) | 16.43 | 🟡 Alert | 0.000 |  |
| 2026-08-03 22:04:36 | Peradeniya (Mahaweli Ganga) | 8.60 | 🟠 Minor Flood | -0.432 |  |
| 2026-08-03 22:04:29 | Kithulgala (Kelani Ganga) | 2.79 | 🟢 Normal | -0.130 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 22:08:02 | Rathnapura (Kalu Ganga) | 8.07 | 🟠 Minor Flood | -0.089 |  |
| 2026-08-03 22:04:36 | Peradeniya (Mahaweli Ganga) | 8.60 | 🟠 Minor Flood | -0.432 |  |
| 2026-08-03 22:04:57 | Glencourse (Kelani Ganga) | 16.43 | 🟡 Alert | 0.000 |  |
| 2026-08-03 22:06:05 | Norwood (Kelani Ganga) | 1.71 | 🟡 Alert | -0.237 |  |
| 2026-08-03 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 4.00 | 🟡 Alert | -0.803 |  |
| 2026-08-03 22:02:44 | Giriulla (Maha Oya) | 4.65 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-08-03 22:02:49 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-08-03 22:08:30 | Hanwella (Kelani Ganga) | 6.77 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-08-03 22:10:09 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-03 22:02:11 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-03 22:11:12 | Magura (Kalu Ganga) | 3.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-03 22:01:15 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-03 22:05:26 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-03 22:06:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 22:36:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 22:05:07 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-03 22:02:46 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:01:16 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:01:47 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:00:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:02:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:02:39 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:02:37 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:03:39 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:03:02 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:01:55 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:05:21 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 22:07:53 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-08-03 22:01:42 | Thawalama (Gin Ganga) | 3.80 | 🟢 Normal | -0.051 |  |
| 2026-08-03 22:06:31 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 22:07:05 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.072 |  |
| 2026-08-03 22:04:29 | Kithulgala (Kelani Ganga) | 2.79 | 🟢 Normal | -0.130 |  |
| 2026-08-03 22:02:09 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.156 |  |
| 2026-08-03 22:05:29 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.333 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)