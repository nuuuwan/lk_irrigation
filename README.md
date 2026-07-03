# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_03:17:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,660 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 03:17:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.008 |  |
| 2026-07-04 03:12:16 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 03:11:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-04 03:10:15 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:09:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:07:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-04 03:07:18 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 03:06:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:06:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:05:02 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 03:05:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-07-04 03:04:50 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.215 |  |
| 2026-07-04 03:04:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 03:04:28 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-04 03:04:23 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:04:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:43 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:05 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:52 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:21 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.100 |  |
| 2026-07-04 03:02:19 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-07-04 03:01:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:00:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 01:18:01 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-04 03:07:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-04 02:11:53 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-04 03:04:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 03:05:02 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 03:07:18 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 03:12:16 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 03:00:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 02:02:09 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:19 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:05 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:04:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:43 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:06:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:52 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:06:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 02:04:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:03:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:04:23 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:02:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 02:01:49 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:10:15 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 03:17:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.008 |  |
| 2026-07-04 03:04:28 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-04 03:11:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-04 03:05:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-07-04 00:03:46 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-07-04 03:01:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-07-04 03:02:21 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.100 |  |
| 2026-07-04 03:04:50 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)