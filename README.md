# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_23:16:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,232 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 23:16:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:14:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:12:06 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-02-14 23:10:13 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:07:57 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-02-14 23:05:56 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:05:35 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:05:00 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:04:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-02-14 23:03:56 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:55 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:54 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:53 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:49 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-14 23:03:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:28 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:21 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:09 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:04 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:49 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-14 23:02:36 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.060 |  |
| 2026-02-14 23:02:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:23 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 23:02:20 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-14 23:01:52 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-14 23:01:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-14 23:00:52 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-14 23:00:48 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 27.000 | 🔺 Rising |
| 2026-02-14 23:00:28 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 27.000 | 🔺 Rising |
| 2026-02-14 22:27:25 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 22:01:54 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-14 23:00:48 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 27.000 | 🔺 Rising |
| 2026-02-14 23:07:57 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-02-14 23:12:06 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-02-14 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-14 23:03:49 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-14 22:00:48 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 23:02:23 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 23:02:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:56 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:01:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 22:27:25 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:21 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:28 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:04 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:05:56 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:05:35 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:16:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:09 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:03:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:14:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 22:01:51 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 22:07:28 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:10:13 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-14 23:02:20 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-14 23:00:52 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-14 22:01:20 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-14 22:03:20 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-02-14 23:02:49 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-14 23:04:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-02-14 21:03:14 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-02-14 23:01:52 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-14 23:02:36 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.060 |  |
| 2026-02-14 21:04:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)