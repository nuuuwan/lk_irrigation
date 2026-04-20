# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_19:26:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,430 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 19:26:01 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-20 19:21:27 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 19:14:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 19:12:50 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-04-20 19:11:31 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-20 19:10:24 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-20 19:10:01 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.052 |  |
| 2026-04-20 19:09:49 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-20 19:08:45 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 19:07:06 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 19:06:20 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:05:43 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-20 19:05:13 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-20 19:05:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:04:57 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.030 |  |
| 2026-04-20 19:04:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:04:36 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:03:57 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-04-20 19:03:42 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:03:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-04-20 19:03:17 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 19:03:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:03:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:02:30 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-04-20 19:02:29 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-20 19:02:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-20 19:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.059 |  |
| 2026-04-20 19:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:01:55 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:01:48 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:01:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-20 19:01:07 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 19:00:40 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:11 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-04-20 19:00:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:57:29 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 19:00:11 | Wellawaya (Kirindi Oya) | 2.10 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-04-20 19:03:57 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-04-20 19:02:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-20 19:05:43 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 19:10:24 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-20 19:05:13 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-20 19:11:31 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-20 19:26:01 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-20 19:01:07 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 19:21:27 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-20 19:09:49 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-20 18:57:29 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 19:14:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 19:03:42 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:05:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:03:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 19:06:20 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 19:07:06 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 19:03:17 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 19:08:45 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 19:01:55 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:02:00 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:40 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:01:48 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:00:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:04:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:03:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:04:36 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:01:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 19:12:50 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-04-20 19:02:29 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-20 19:02:30 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-04-20 19:04:57 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.030 |  |
| 2026-04-20 19:10:01 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.052 |  |
| 2026-04-20 19:03:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-04-20 19:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)