# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_17:16:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 17:16:56 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-05 17:15:42 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:13:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:13:01 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:12:57 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:11:39 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.036 |  |
| 2026-06-05 17:10:31 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:09:48 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-05 17:07:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:07:20 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-05 17:06:58 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:06:04 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.074 |  |
| 2026-06-05 17:05:32 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:05:28 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.076 |  |
| 2026-06-05 17:05:02 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 17:04:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:04:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:04:44 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-06-05 17:03:42 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.040 |  |
| 2026-06-05 17:03:31 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:03:13 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-05 17:02:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:02:27 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:02:22 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.107 |  |
| 2026-06-05 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.020 |  |
| 2026-06-05 17:02:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-05 17:02:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:01:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:01:33 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:01:14 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:01:12 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:01:11 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:00:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:00:22 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:00:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.056 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 16:09:48 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-05 17:00:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-05 17:09:48 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-05 17:03:13 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-05 17:07:20 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-05 17:05:02 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 17:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:01:11 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:03:31 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:06:58 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:15:42 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 17:16:56 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-05 17:00:22 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:00:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:04:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:02:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:05:32 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:07:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:02:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:01:33 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:12:57 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:04:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:01:12 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:13:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:10:31 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:13:01 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-06-05 17:01:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:02:27 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:01:14 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:02:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-05 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.020 |  |
| 2026-06-05 17:04:44 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-06-05 16:03:41 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-06-05 17:11:39 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.036 |  |
| 2026-06-05 17:03:42 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.040 |  |
| 2026-06-05 17:06:04 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.074 |  |
| 2026-06-05 17:05:28 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.076 |  |
| 2026-06-05 17:02:22 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)