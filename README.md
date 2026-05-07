# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_23:16:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,687 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 23:16:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-05-07 23:10:55 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.048 |  |
| 2026-05-07 23:07:49 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.028 |  |
| 2026-05-07 23:07:26 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:07:17 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-07 23:06:59 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.318 |  |
| 2026-05-07 23:06:37 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.128 |  |
| 2026-05-07 23:06:13 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.022 |  |
| 2026-05-07 23:05:30 | Thanamalwila (Kirindi Oya) | 2.85 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-07 23:05:16 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.147 |  |
| 2026-05-07 23:05:01 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 23:04:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:04:06 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 23:03:02 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:02:58 | Kuda Oya (Kirindi Oya) | 3.80 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-07 23:02:58 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-05-07 23:02:54 | Nakkala (Kumbukkan Oya) | 2.25 | 🟢 Normal | -0.336 |  |
| 2026-05-07 23:02:43 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-05-07 23:02:36 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-07 23:02:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:01:58 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-05-07 23:01:54 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-05-07 23:01:53 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:01:52 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 23:01:35 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 23:01:31 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:01:26 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-05-07 23:01:26 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.050 |  |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-07 23:00:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-07 23:02:43 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-05-07 23:01:54 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-05-07 23:05:01 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 23:05:30 | Thanamalwila (Kirindi Oya) | 2.85 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-07 23:01:26 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-05-07 23:02:58 | Kuda Oya (Kirindi Oya) | 3.80 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-07 23:07:17 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-07 23:01:35 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 23:04:06 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 23:01:52 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 23:07:26 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:14 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:03:02 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:01:31 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:01:53 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:02:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:00:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 23:04:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-07 23:02:36 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-07 23:01:58 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-05-07 23:06:13 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.022 |  |
| 2026-05-07 23:07:49 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.028 |  |
| 2026-05-07 22:04:44 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.029 |  |
| 2026-05-07 23:16:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-05-07 22:01:20 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.038 |  |
| 2026-05-07 23:10:55 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.048 |  |
| 2026-05-07 23:01:26 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.050 |  |
| 2026-05-07 22:07:35 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.056 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-07 23:02:58 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-05-07 23:06:37 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.128 |  |
| 2026-05-07 23:05:16 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.147 |  |
| 2026-05-07 22:00:43 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.235 |  |
| 2026-05-07 23:06:59 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.318 |  |
| 2026-05-07 23:02:54 | Nakkala (Kumbukkan Oya) | 2.25 | 🟢 Normal | -0.336 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)