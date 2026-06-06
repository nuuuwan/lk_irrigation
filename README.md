# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_19:15:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 19:15:50 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.008 |  |
| 2026-06-06 19:12:34 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:10:56 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:10:10 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:09:28 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.018 |  |
| 2026-06-06 19:08:24 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:08:09 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-06 19:07:48 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.028 |  |
| 2026-06-06 19:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 19:01:28 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-06 19:03:19 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 19:05:14 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-06 19:08:09 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:02:57 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:01:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:01:27 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:08:24 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:01:54 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:10:10 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:02:47 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:02:38 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:05:22 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:03:21 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 19:15:50 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.008 |  |
| 2026-06-06 19:05:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2026-06-06 19:10:56 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:04:40 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:12:34 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-06-06 19:02:20 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-06-06 19:01:11 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-06-06 19:09:28 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.018 |  |
| 2026-06-06 19:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.019 |  |
| 2026-06-06 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-06-06 19:07:48 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.028 |  |
| 2026-06-06 19:03:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-06-06 19:03:20 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.039 |  |
| 2026-06-06 19:02:34 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.039 |  |
| 2026-06-06 19:03:53 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-06 19:04:12 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.059 |  |
| 2026-06-06 19:06:18 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.068 |  |
| 2026-06-06 19:01:32 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | -0.090 |  |
| 2026-06-06 19:05:05 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.092 |  |
| 2026-06-06 19:04:10 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.100 |  |
| 2026-06-06 19:04:48 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.508 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)