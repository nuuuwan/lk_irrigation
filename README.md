# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_02:11:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 02:11:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.029 |  |
| 2026-03-20 02:10:23 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-03-20 02:07:05 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.164 |  |
| 2026-03-20 02:06:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:05:55 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-20 02:04:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-20 02:04:40 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-20 02:04:29 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:55 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:42 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 02:03:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-20 02:03:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 02:03:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-20 02:03:15 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:14 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 02:02:32 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:02:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:02:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-20 02:02:26 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-20 02:02:22 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.093 |  |
| 2026-03-20 02:02:01 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:01:54 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:01:35 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.233 |  |
| 2026-03-20 02:01:25 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-03-20 02:01:22 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 02:00:59 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:00:52 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.128 |  |
| 2026-03-20 02:00:38 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.050 |  |
| 2026-03-20 01:51:18 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 01:51:09 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.029 |  |
| 2026-03-20 01:37:45 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:27:27 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 01:01:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-20 02:04:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 02:02:26 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-20 02:03:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 02:03:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-20 02:03:42 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 02:01:22 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 01:37:45 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 02:04:29 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:02:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:06:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:01:54 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:15 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:02:01 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:02:32 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:55 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:00:59 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:02 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-20 02:01:25 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-03-20 02:05:55 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-20 02:04:40 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-20 02:02:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-03-20 01:11:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-03-20 02:11:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.029 |  |
| 2026-03-20 02:10:23 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-03-19 22:04:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-03-20 02:00:38 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.050 |  |
| 2026-03-20 02:02:22 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.093 |  |
| 2026-03-20 02:00:52 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.128 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-20 02:07:05 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.164 |  |
| 2026-03-20 02:01:35 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)