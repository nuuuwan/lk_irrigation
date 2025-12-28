# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_16:35:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 16:35:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.007 |  |
| 2025-12-28 16:32:10 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:10:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-28 16:09:47 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.036 |  |
| 2025-12-28 16:09:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-28 16:08:54 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:08:11 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.047 |  |
| 2025-12-28 16:07:17 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:07:05 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:07:04 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:06:52 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2025-12-28 16:06:46 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.056 |  |
| 2025-12-28 16:06:08 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:05:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:04:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:04:54 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-28 16:04:53 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:04:50 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:04:19 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-28 16:03:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:03:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:03:17 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:03:11 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 16:03:08 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:02:58 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:46 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:45 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 16:02:30 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2025-12-28 16:01:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:01:12 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:01:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:01:02 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-28 16:00:59 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:45 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 16:04:54 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-28 16:09:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-28 16:01:02 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-28 16:04:19 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-28 16:03:11 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 16:02:45 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 16:10:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-28 16:02:58 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 16:03:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:07:17 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:30 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:59 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:08:54 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:46 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:32:10 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:05:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:04:50 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:02:46 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:06:08 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:03:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:06:46 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:07:04 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:00:45 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:07:05 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:04:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 16:35:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.007 |  |
| 2025-12-28 16:06:52 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2025-12-28 16:01:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:03:17 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:03:08 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:04:53 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:10 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:01:12 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:00:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-28 16:09:47 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.036 |  |
| 2025-12-28 16:08:11 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.047 |  |
| 2025-12-28 16:02:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2025-12-28 16:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)