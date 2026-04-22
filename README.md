# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_06:24:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 06:24:21 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-04-22 06:12:49 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-22 06:11:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-22 06:09:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-04-22 06:08:24 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-04-22 06:08:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:07:52 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:07:41 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:07:34 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-22 06:07:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-04-22 06:07:24 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 06:07:13 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-22 06:06:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:06:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.303 |  |
| 2026-04-22 06:05:08 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 06:04:36 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-22 06:04:17 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 06:04:03 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.153 |  |
| 2026-04-22 06:03:35 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 06:03:33 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 06:03:27 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-22 06:03:21 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-04-22 06:03:19 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.248 |  |
| 2026-04-22 06:03:18 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-22 06:02:48 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-04-22 06:02:36 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.060 |  |
| 2026-04-22 06:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-22 06:02:03 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 06:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:32 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-22 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-04-22 06:01:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 06:00:30 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-04-22 06:00:25 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-04-22 05:59:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 06:03:27 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-22 06:12:49 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-22 06:02:03 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 06:04:17 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 06:05:08 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 06:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-22 06:07:13 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-22 06:03:33 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 06:01:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 06:07:24 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 06:04:36 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-22 06:03:18 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-22 06:03:35 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 06:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:06:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:07:52 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:08:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:07:41 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:05:08 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.005 |  |
| 2026-04-22 06:07:34 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-22 06:08:24 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-04-22 06:11:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-22 06:02:48 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-04-22 06:01:32 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-22 06:07:33 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-04-22 06:00:30 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-04-22 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-04-22 06:03:21 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-04-22 06:24:21 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-04-22 06:09:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-04-22 06:02:36 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.060 |  |
| 2026-04-22 05:59:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.064 |  |
| 2026-04-22 06:00:25 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-04-22 06:04:03 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.153 |  |
| 2026-04-22 06:03:19 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.248 |  |
| 2026-04-22 06:06:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.303 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)