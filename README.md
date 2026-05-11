# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_07:26:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,674 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 07:26:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.056 |  |
| 2026-05-11 07:25:27 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-11 07:21:35 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:12:08 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.017 |  |
| 2026-05-11 07:11:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-11 07:10:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:09:53 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-11 07:09:38 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.055 |  |
| 2026-05-11 07:09:12 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | -0.026 |  |
| 2026-05-11 07:08:52 | Katharagama (Menik Ganga) | 1.69 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-11 07:08:24 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-11 07:08:05 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-05-11 07:07:57 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-11 07:07:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-11 07:07:06 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | -0.648 |  |
| 2026-05-11 07:06:51 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-11 07:06:19 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 07:06:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-11 07:05:08 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-11 07:05:04 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.039 |  |
| 2026-05-11 07:04:51 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:04:48 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 07:04:47 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-05-11 07:04:31 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-11 07:04:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:02:55 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-05-11 07:02:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 07:02:00 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 07:01:39 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 07:01:36 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 07:01:26 | Kuda Oya (Kirindi Oya) | 3.48 | 🟢 Normal | -0.438 |  |
| 2026-05-11 07:01:11 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.021 |  |
| 2026-05-11 07:01:05 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.069 |  |
| 2026-05-11 07:00:39 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -18.000 |  |
| 2026-05-11 07:00:37 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -18.000 |  |
| 2026-05-11 07:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 06:00:26 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-11 07:11:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-11 06:30:44 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-11 07:09:53 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-11 07:08:24 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-11 07:04:31 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-11 07:08:52 | Katharagama (Menik Ganga) | 1.69 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-11 07:07:57 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-11 07:01:39 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 07:02:00 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 07:07:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-11 07:25:27 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-11 07:02:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 07:04:48 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 07:06:19 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 07:01:36 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 07:04:51 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:21:35 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:10:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:04:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 07:06:51 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-11 07:05:08 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-11 07:12:08 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.017 |  |
| 2026-05-11 07:04:47 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-05-11 07:01:11 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.021 |  |
| 2026-05-11 07:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-11 07:09:12 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | -0.026 |  |
| 2026-05-11 07:06:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-11 07:02:55 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-05-11 07:08:05 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-05-11 07:05:04 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.039 |  |
| 2026-05-11 07:09:38 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.055 |  |
| 2026-05-11 07:26:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.056 |  |
| 2026-05-11 07:01:05 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.069 |  |
| 2026-05-11 07:01:26 | Kuda Oya (Kirindi Oya) | 3.48 | 🟢 Normal | -0.438 |  |
| 2026-05-11 07:07:06 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | -0.648 |  |
| 2026-05-11 07:00:39 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)