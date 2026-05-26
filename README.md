# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_05:36:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,855 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 05:36:05 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-26 05:29:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:26:57 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 05:20:41 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.025 |  |
| 2026-05-26 05:16:11 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.016 |  |
| 2026-05-26 05:11:39 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:10:53 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:10:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:10:23 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:09:41 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 05:08:27 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 05:07:37 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:07:07 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.381 |  |
| 2026-05-26 05:06:44 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-26 05:06:41 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | 0.426 | 🔺 Rising |
| 2026-05-26 05:06:34 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-26 05:06:25 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-05-26 05:05:45 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-26 05:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-05-26 05:04:49 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 05:04:44 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 05:04:19 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:04:05 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:03:00 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:02:40 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:02:32 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-26 05:02:28 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-26 05:01:59 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-26 05:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:01:38 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-26 05:00:49 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:00:19 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 05:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-05-26 05:06:41 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | 0.426 | 🔺 Rising |
| 2026-05-26 05:01:59 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-26 05:06:34 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-26 05:06:44 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-26 05:36:05 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-26 05:05:45 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-26 05:04:44 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 05:08:27 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 05:26:57 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 05:04:49 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 05:09:41 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 04:06:25 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-26 04:02:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:04:03 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:10:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:29:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:07:37 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:02:40 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:04:05 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:00:49 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:00:19 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:04:19 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:11:39 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:03:00 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 05:02:28 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-26 05:02:32 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 05:01:38 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 05:16:11 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.016 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:02:49 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-26 05:20:41 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.025 |  |
| 2026-05-26 05:06:25 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-05-26 05:07:07 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)