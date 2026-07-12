# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_05:06:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,814 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 05:06:08 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:05:48 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:05:28 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:05:28 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-13 05:05:23 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:04:34 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:04:31 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-07-13 05:03:49 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:21 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:12 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:02:20 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:02:05 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-13 05:02:00 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.270 |  |
| 2026-07-13 05:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:19 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-13 05:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:02 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 05:00:58 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:49 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:31 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:17 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-13 05:00:12 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-07-13 04:59:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-13 04:39:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 04:39:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 04:38:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 04:38:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 04:37:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 04:37:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 4.154 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 04:39:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-07-13 05:01:19 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-13 05:05:28 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-13 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-13 05:01:02 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 04:59:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:04:34 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:49 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:21 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:02:26 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 03:06:46 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:05:23 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:12 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:06:08 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:05:28 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:17 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:31 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:02:20 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-13 04:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-13 04:08:00 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:03:49 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 04:02:17 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:01:22 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-13 05:00:58 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 03:05:42 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 03:07:37 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2026-07-13 05:04:31 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-07-13 05:02:05 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-13 05:00:12 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-07-13 04:10:51 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.056 |  |
| 2026-07-13 04:04:59 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.081 |  |
| 2026-07-13 04:16:29 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.128 |  |
| 2026-07-13 05:02:00 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)