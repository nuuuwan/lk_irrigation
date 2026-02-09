# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_20:18:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,653 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 20:18:59 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-02-09 20:12:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-09 20:12:28 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 20:11:54 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:11:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-02-09 20:10:49 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 20:10:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:09:50 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-09 20:09:29 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:08:59 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.047 |  |
| 2026-02-09 20:07:21 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:06:34 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:54 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:48 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:46 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:22 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:05:15 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:11 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-09 20:04:56 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:04:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:04:19 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:03:31 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:03:31 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:03:05 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:02:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:02:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |
| 2026-02-09 20:02:38 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:02:29 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:01:53 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-02-09 20:01:53 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:51 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:49 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:01:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-02-09 20:01:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:12 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 19:02:28 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-02-09 20:05:11 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-09 20:09:50 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-09 20:12:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-09 20:10:49 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 20:02:29 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:01:49 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:05:22 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:03:31 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 20:12:28 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 20:05:46 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:02:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:15 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:53 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:07:21 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:06:34 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:03:05 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:02:38 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:04:56 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:03:31 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:51 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:04:19 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:01:12 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:11:54 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:10:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:09:29 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:54 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 20:05:48 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-09 20:01:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-02-09 20:18:59 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-02-09 20:11:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-02-09 20:01:53 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-02-09 20:08:59 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.047 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-09 20:02:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)