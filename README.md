# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_18:47:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,354 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:38:12 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:21:25 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.007 |  |
| 2026-07-03 18:18:29 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-07-03 18:13:39 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:12:18 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:11:28 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-07-03 18:10:10 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-03 18:09:48 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-03 18:09:14 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:08:52 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 18:06:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.078 |  |
| 2026-07-03 18:06:56 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-03 18:05:06 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:05:06 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.038 |  |
| 2026-07-03 18:04:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:38 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-03 18:04:25 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:04:20 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:07 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:03:34 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:03:09 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 18:03:07 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 18:03:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.059 |  |
| 2026-07-03 18:02:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-07-03 18:02:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 18:02:08 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:39 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:38 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:36 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-07-03 18:01:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 18:06:56 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-03 18:03:09 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-03 18:04:38 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-03 18:10:10 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-03 18:03:07 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 18:08:52 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 18:00:10 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:12:18 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:38 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:05:06 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:08 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:25 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:13:39 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:16 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:07 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:03:34 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:48 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:01:39 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:38:12 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:02:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:04:20 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-03 18:21:25 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.007 |  |
| 2026-07-03 18:18:29 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-07-03 18:04:22 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:02:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-07-03 18:11:28 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-07-03 18:00:19 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-07-03 18:05:06 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.038 |  |
| 2026-07-03 18:01:36 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-07-03 18:03:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.059 |  |
| 2026-07-03 18:06:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)