# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_14:28:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,934 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 14:28:54 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:23:15 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-26 14:22:41 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-06-26 14:22:18 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-26 14:16:29 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 14:15:48 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:09:44 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:07:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 14:06:49 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 14:06:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-26 14:06:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:06:32 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:06:09 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-26 14:05:50 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.019 |  |
| 2026-06-26 14:05:37 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:05:20 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 14:05:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 14:04:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:04:31 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-26 14:04:03 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-06-26 14:03:56 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:03:28 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.054 |  |
| 2026-06-26 14:03:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.017 |  |
| 2026-06-26 14:03:10 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 14:02:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:02:55 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:50 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:28 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:09 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 14:06:09 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-26 14:03:10 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 14:04:31 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-26 14:22:18 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-26 14:07:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 14:05:20 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 14:16:29 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 14:06:49 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 14:05:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 14:23:15 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-26 14:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:05:37 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:01:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:00:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:28:54 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:15:48 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:04:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:03:56 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:55 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:06:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:00:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:50 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:00:51 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:09:44 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:00:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:09 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 14:22:41 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-06-26 14:02:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:06:32 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:02:28 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-26 14:04:03 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-06-26 14:03:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.017 |  |
| 2026-06-26 14:06:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-26 14:05:50 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.019 |  |
| 2026-06-26 14:01:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.047 |  |
| 2026-06-26 14:03:28 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)