# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_07:21:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 07:21:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:20:00 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.053 |  |
| 2026-01-06 07:14:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:13:54 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 07:13:12 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:12:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 07:11:20 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-01-06 07:11:07 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.344 |  |
| 2026-01-06 07:07:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-06 07:07:38 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.344 |  |
| 2026-01-06 07:04:41 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 07:04:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-06 07:04:18 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 07:04:16 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:04:07 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:04:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:03:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.165 |  |
| 2026-01-06 07:03:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.012 |  |
| 2026-01-06 07:03:39 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.020 |  |
| 2026-01-06 07:03:38 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-06 07:03:30 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-01-06 07:03:30 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:03:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-06 07:03:19 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-01-06 07:03:16 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-06 07:03:16 | Siyambalanduwa (Heda Oya) | 4.15 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-01-06 07:03:06 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.151 |  |
| 2026-01-06 07:03:05 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-01-06 07:02:53 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-01-06 07:02:22 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-06 07:02:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:01:47 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 07:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:01:36 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-06 07:01:35 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 07:01:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:01:01 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-06 06:34:16 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 07:03:16 | Siyambalanduwa (Heda Oya) | 4.15 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-01-06 07:03:30 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-01-06 07:03:16 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-06 07:02:53 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-01-06 07:02:22 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-06 07:13:54 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 07:03:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-06 07:01:36 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-06 07:01:35 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 07:01:47 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 06:10:12 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-06 07:07:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-06 07:04:41 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 07:04:18 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 07:01:01 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-06 07:04:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:04:07 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:04:16 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:03:05 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 07:12:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 07:02:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:13:12 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:01:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:03:30 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:14:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:21:41 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 07:04:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-06 07:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-01-06 07:03:38 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-06 06:02:26 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-01-06 07:03:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.012 |  |
| 2026-01-06 07:11:20 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-01-06 07:03:39 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.020 |  |
| 2026-01-06 07:20:00 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.053 |  |
| 2026-01-06 07:03:19 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-01-06 07:03:06 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.151 |  |
| 2026-01-06 07:03:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.165 |  |
| 2026-01-06 07:11:07 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)