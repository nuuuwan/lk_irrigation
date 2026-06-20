# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_16:19:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 16:19:48 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-20 16:14:59 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.008 |  |
| 2026-06-20 16:14:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-20 16:14:39 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-20 16:12:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:11:23 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 16:10:15 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:08:45 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:07:52 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:05:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:05:58 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:05:28 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.093 |  |
| 2026-06-20 16:05:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-06-20 16:04:55 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-06-20 16:04:42 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:04:14 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:03:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-20 16:03:18 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-20 16:03:16 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:10 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:08 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.039 |  |
| 2026-06-20 16:02:34 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.070 |  |
| 2026-06-20 16:02:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-20 16:01:55 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-20 16:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:01:37 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:02 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:01 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 16:02:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-20 16:03:21 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-20 16:03:18 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-20 16:14:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-20 16:19:48 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-20 15:02:50 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 16:11:23 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 16:01:01 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:12:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:08:45 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:10 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:37 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:04:14 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:05:58 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:56 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:16 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:05:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:04:42 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:02:34 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:07:52 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:01:02 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:14:59 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.008 |  |
| 2026-06-20 16:14:39 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-20 16:10:15 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:03:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:01:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:05:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-06-20 16:01:55 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-20 16:04:55 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-06-20 15:03:03 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-06-20 16:03:08 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.039 |  |
| 2026-06-20 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.070 |  |
| 2026-06-20 16:05:28 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)