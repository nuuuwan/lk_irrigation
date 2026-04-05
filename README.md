# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_19:23:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 19:23:50 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:18:54 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-04-05 19:16:02 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-05 19:14:31 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.033 |  |
| 2026-04-05 19:12:15 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:12:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.017 |  |
| 2026-04-05 19:11:13 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-05 19:09:18 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-05 19:07:18 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.027 |  |
| 2026-04-05 19:06:00 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-05 19:05:21 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:05:13 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:05:12 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 19:05:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-05 19:04:57 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-04-05 19:04:31 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.056 |  |
| 2026-04-05 19:04:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-04-05 19:04:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:03:51 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 19:03:42 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:03:15 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 19:03:14 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:03:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:02:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:29 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-05 19:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:05 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:37 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:19 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:00:12 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 19:02:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-05 19:16:02 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-05 19:11:13 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-05 19:09:18 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-05 19:03:51 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 19:03:15 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 19:00:12 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:23:50 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:04:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:05 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:03:14 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:29 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:05:21 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:19 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:03:42 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:02:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:01:37 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:18:54 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-04-05 19:06:00 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-05 19:12:15 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:03:01 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:05:13 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 19:12:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.017 |  |
| 2026-04-05 19:05:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-05 19:05:12 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 19:07:18 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.027 |  |
| 2026-04-05 19:04:57 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-04-05 19:14:31 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.033 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.053 |  |
| 2026-04-05 19:04:31 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.056 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 19:04:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)