# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_18:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,568 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 18:13:50 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-05-24 18:12:34 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 18:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.22 | 🟡 Alert | -0.038 |  |
| 2026-05-24 18:08:04 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 18:07:07 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.073 |  |
| 2026-05-24 18:06:57 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:05:51 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:05:32 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:05:12 | Ellagawa (Kalu Ganga) | 9.65 | 🟢 Normal | -0.048 |  |
| 2026-05-24 18:04:58 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-24 18:04:32 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:04:11 | Deraniyagala (Kelani Ganga) | 2.76 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2026-05-24 18:03:57 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:38 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-24 18:03:37 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-24 18:03:36 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 18:03:34 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:27 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.021 |  |
| 2026-05-24 18:03:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:40 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 18:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-24 18:02:20 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | -0.082 |  |
| 2026-05-24 18:02:08 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:07 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:00 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-24 18:01:58 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:01:25 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-05-24 18:01:22 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 17:46:26 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 18:02:40 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 18:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.22 | 🟡 Alert | -0.038 |  |
| 2026-05-24 18:04:11 | Deraniyagala (Kelani Ganga) | 2.76 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2026-05-24 18:03:38 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-24 18:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-24 18:08:04 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 18:03:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 18:01:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:01:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:12:34 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:05:51 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:06:57 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:34 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:07 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:58 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:02:08 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:04:32 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:22 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:03:36 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:01:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:05:32 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:13:50 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-05-24 18:03:37 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-24 18:02:00 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-24 18:04:58 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-24 18:03:27 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.021 |  |
| 2026-05-24 18:01:25 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-05-24 17:04:44 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-24 18:05:12 | Ellagawa (Kalu Ganga) | 9.65 | 🟢 Normal | -0.048 |  |
| 2026-05-24 18:07:07 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.073 |  |
| 2026-05-24 18:02:20 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)