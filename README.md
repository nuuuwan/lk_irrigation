# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_02:28:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 02:28:01 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.056 |  |
| 2026-05-08 02:22:59 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-08 02:17:46 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -90.000 |  |
| 2026-05-08 02:17:44 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -90.000 |  |
| 2026-05-08 02:13:13 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:12:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-08 02:09:14 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.227 |  |
| 2026-05-08 02:08:45 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.223 |  |
| 2026-05-08 02:07:05 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-05-08 02:06:47 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-05-08 02:06:43 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-05-08 02:06:09 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:06:08 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:05:48 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-08 02:05:31 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.080 |  |
| 2026-05-08 02:05:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:05:05 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.131 |  |
| 2026-05-08 02:05:04 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-08 02:04:38 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 02:03:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.166 |  |
| 2026-05-08 02:03:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:03:18 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-05-08 02:03:01 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:02:49 | Giriulla (Maha Oya) | 2.52 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-05-08 02:02:31 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:02:23 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.176 |  |
| 2026-05-08 02:02:21 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:02:03 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-05-08 02:01:18 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-05-08 02:00:29 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-05-08 02:00:23 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.072 |  |
| 2026-05-08 02:00:14 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 02:02:49 | Giriulla (Maha Oya) | 2.52 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-05-08 02:00:29 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-05-08 02:05:04 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-08 02:01:18 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-05-08 02:22:59 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-08 02:04:38 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 02:00:14 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-08 01:04:43 | Thanamalwila (Kirindi Oya) | 3.51 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 02:12:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-08 02:13:13 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:03:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:01:08 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:06:09 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:03:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:02:31 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:05:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-08 02:03:01 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 01:12:04 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-08 02:05:48 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 01:04:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-05-08 02:02:03 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-05-08 02:03:18 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-05-08 02:07:05 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-05-08 02:28:01 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.056 |  |
| 2026-05-08 02:06:47 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-05-08 02:06:43 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 02:00:23 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.072 |  |
| 2026-05-08 02:05:31 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.080 |  |
| 2026-05-08 02:05:05 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.131 |  |
| 2026-05-08 02:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.166 |  |
| 2026-05-08 02:02:23 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.176 |  |
| 2026-05-08 01:01:12 | Kuda Oya (Kirindi Oya) | 3.52 | 🟢 Normal | -0.215 |  |
| 2026-05-08 02:08:45 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.223 |  |
| 2026-05-08 02:09:14 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.227 |  |
| 2026-05-08 02:17:46 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)