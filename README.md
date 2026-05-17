# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_02:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 02:02:52 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:02:42 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.096 |  |
| 2026-05-18 02:02:37 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-18 02:02:28 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | -0.088 |  |
| 2026-05-18 02:02:24 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:59 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -1.029 |  |
| 2026-05-18 02:01:50 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:47 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:43 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.262 |  |
| 2026-05-18 02:01:40 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:24 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -1.029 |  |
| 2026-05-18 02:01:21 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-18 02:01:16 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-05-18 02:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:00:17 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:46:59 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.008 |  |
| 2026-05-18 01:44:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-18 01:38:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:37:52 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:38 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:06 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.025 |  |
| 2026-05-18 01:12:27 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.096 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 21:00:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.064 |  |
| 2026-05-18 01:02:35 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-18 01:44:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-18 00:17:17 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-18 01:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 02:00:17 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:05:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:50 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:40 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:03:23 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:47 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:38:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:38 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:20 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:02:24 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:32 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:02:52 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:46:59 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.008 |  |
| 2026-05-18 01:08:10 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:02:06 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-05-18 02:01:21 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-18 01:05:48 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:06:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:04:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:16:06 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.025 |  |
| 2026-05-18 01:06:08 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-05-18 02:01:16 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-05-18 02:02:37 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-18 00:04:14 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.048 |  |
| 2026-05-18 01:05:33 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.060 |  |
| 2026-05-18 02:02:28 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | -0.088 |  |
| 2026-05-18 02:02:42 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.096 |  |
| 2026-05-18 02:01:43 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.262 |  |
| 2026-05-18 02:01:59 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -1.029 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)