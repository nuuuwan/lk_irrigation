# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_19:21:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 19:21:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.015 |  |
| 2026-04-06 19:10:56 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 19:10:43 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-06 19:10:10 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-06 19:10:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-06 19:08:37 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:08:36 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 19:08:17 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:06:55 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-06 19:06:50 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-06 19:06:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:05:28 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-06 19:05:07 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-06 19:05:02 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:52 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.088 |  |
| 2026-04-06 19:03:43 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:31 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 19:03:26 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:07 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-06 19:02:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.126 |  |
| 2026-04-06 19:02:34 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-06 19:02:18 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-06 19:02:16 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-06 19:02:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:09 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:00 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:53 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:51 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:45 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:28 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:20 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:00:50 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 19:06:55 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-06 19:05:07 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-06 19:02:34 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-06 19:03:31 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 19:06:50 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-06 19:10:43 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-06 19:10:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-06 19:08:36 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 19:10:56 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 19:01:53 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:09 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:51 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:28 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:08:17 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:07 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:08:37 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:26 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:05:02 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:01:20 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:03:43 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:16 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:06:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:02:00 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 19:10:10 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-06 19:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-06 19:05:28 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-06 19:00:50 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-04-06 19:21:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.015 |  |
| 2026-04-06 19:02:55 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-06 19:02:18 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 19:03:52 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.088 |  |
| 2026-04-06 19:02:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)