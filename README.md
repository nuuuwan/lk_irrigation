# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_03:34:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 03:34:44 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-30 03:30:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:16:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -36.000 |  |
| 2025-12-30 03:16:47 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -36.000 |  |
| 2025-12-30 03:16:46 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -36.000 |  |
| 2025-12-30 03:16:45 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -36.000 |  |
| 2025-12-30 03:16:43 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -36.000 |  |
| 2025-12-30 03:12:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:11:33 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:11:17 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:51 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:11 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:10:01 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:08:15 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-30 03:06:03 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:05:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:05:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:05:02 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:04:50 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 03:04:41 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:04:23 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:03:29 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:03:20 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:03:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:01:58 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.005 |  |
| 2025-12-30 03:01:44 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.151 |  |
| 2025-12-30 03:01:36 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:01:31 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:01:30 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.032 |  |
| 2025-12-30 02:59:12 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 01:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-30 03:04:50 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 03:34:44 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 03:01:58 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.005 |  |
| 2025-12-30 03:02:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:01:36 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:04:41 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:59:12 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:06:03 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:30:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:05:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-30 00:09:20 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:03:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:02:55 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:02:12 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:02:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:51 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:00:55 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:02:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:12:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:01:14 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.005 |  |
| 2025-12-30 03:08:15 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-30 03:04:33 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:10:11 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:03:29 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:03:20 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:01:31 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.010 |  |
| 2025-12-30 03:05:02 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:05:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:04:23 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2025-12-30 03:01:30 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.032 |  |
| 2025-12-30 03:01:44 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.151 |  |
| 2025-12-30 03:16:48 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)