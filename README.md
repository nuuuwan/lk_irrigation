# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_05:13:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 05:13:41 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-05 05:08:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 05:07:51 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-01-05 05:06:28 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-01-05 05:06:20 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-01-05 05:06:02 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 05:05:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.014 |  |
| 2026-01-05 05:05:05 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:04:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:04:31 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:04:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-01-05 05:04:00 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.022 |  |
| 2026-01-05 05:03:52 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 05:03:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:03:07 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.033 |  |
| 2026-01-05 05:03:03 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:03:00 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:02:49 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:47 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:46 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:46 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 05:02:45 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.207 |  |
| 2026-01-05 05:02:44 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:17 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-05 05:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-01-05 05:02:00 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-05 05:01:48 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 05:01:43 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 05:01:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:01:35 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-05 05:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.036 |  |
| 2026-01-05 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:01:14 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:00:48 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:00:42 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:50:37 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-01-05 04:49:37 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-01-05 04:46:48 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-01-05 04:43:54 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.006 |  |
| 2026-01-05 04:27:47 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.036 |  |
| 2026-01-05 04:26:21 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:22:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.014 |  |
| 2026-01-05 04:22:21 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.014 |  |
| 2026-01-05 04:21:27 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 05:02:49 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-05 05:02:17 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-05 05:02:46 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 02:17:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 05:02:00 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-05 05:01:43 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 05:01:48 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 05:03:52 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 05:08:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 05:00:48 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:03:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:00:42 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:03:00 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:01:14 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:01:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:05:05 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:03:03 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:09:04 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:04:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 05:04:31 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:43:54 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.006 |  |
| 2026-01-05 05:13:41 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-05 05:06:02 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 05:05:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.014 |  |
| 2026-01-05 05:04:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-01-05 05:06:20 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-01-05 05:04:00 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.022 |  |
| 2026-01-05 05:07:51 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-01-05 05:03:07 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.033 |  |
| 2026-01-05 05:01:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.036 |  |
| 2026-01-05 05:06:28 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-01-05 05:01:35 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-05 05:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-01-05 05:02:45 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)