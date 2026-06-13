# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_20:18:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 20:18:54 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-06-13 20:11:03 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.017 |  |
| 2026-06-13 20:10:03 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:09:55 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 20:09:54 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:07:43 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:06:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:06:30 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:06:22 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.023 |  |
| 2026-06-13 20:05:47 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.060 |  |
| 2026-06-13 20:05:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:04:32 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:04:25 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:04:16 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:04:12 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 20:04:05 | Magura (Kalu Ganga) | 4.01 | 🟡 Alert | -0.020 |  |
| 2026-06-13 20:04:03 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.014 |  |
| 2026-06-13 20:03:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:03:28 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:03:27 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:03:20 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-13 20:03:08 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.030 |  |
| 2026-06-13 20:03:01 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.028 |  |
| 2026-06-13 20:02:58 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 20:02:33 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-06-13 20:02:26 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 20:02:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:01:53 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:01:49 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-06-13 20:01:47 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:01:47 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-06-13 20:01:01 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 20:00:49 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 20:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-06-13 20:04:05 | Magura (Kalu Ganga) | 4.01 | 🟡 Alert | -0.020 |  |
| 2026-06-13 20:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-13 20:00:49 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 20:01:01 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 20:04:12 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 20:09:55 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 20:02:26 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 20:02:58 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 20:01:47 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:06:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:04:25 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:18:54 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:02:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:09:54 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:03:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:01:47 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:07:43 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:10:03 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:05:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-13 20:04:32 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:01:53 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:03:20 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:06:30 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-06-13 20:02:33 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-06-13 20:01:49 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-06-13 20:04:03 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.014 |  |
| 2026-06-13 20:11:03 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.017 |  |
| 2026-06-13 20:03:28 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:04:16 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:03:27 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-06-13 20:06:22 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.023 |  |
| 2026-06-13 20:03:01 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.028 |  |
| 2026-06-13 20:03:08 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.030 |  |
| 2026-06-13 20:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 20:05:47 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)