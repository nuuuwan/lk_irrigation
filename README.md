# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_18:16:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 18:16:42 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:13:36 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-18 18:12:57 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:10:08 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:09:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:09:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.151 |  |
| 2026-04-18 18:08:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:07:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:07:29 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:06:40 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-18 18:06:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:05:56 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:05:27 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:04:39 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-04-18 18:04:15 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:03:49 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-18 18:03:49 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-04-18 18:03:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-04-18 18:03:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:03:27 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-04-18 18:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:02:35 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 18:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:02:22 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-04-18 18:02:18 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:02:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-04-18 18:02:10 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.102 |  |
| 2026-04-18 18:01:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-18 18:01:40 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-18 18:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:20 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:00:54 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:00:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:00:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:00:12 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.121 |  |
| 2026-04-18 17:48:21 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:48:03 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:39:49 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 18:03:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-04-18 18:06:40 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-18 18:01:40 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-18 18:03:49 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-18 17:00:36 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-18 18:02:35 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 18:01:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-18 18:00:54 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:00:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:03:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:07:44 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:12:57 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:09:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:08:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:04:15 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:05:27 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:16:42 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:02:18 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:05:56 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:07:29 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:10:08 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:06:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:00:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 18:13:36 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-18 18:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:20 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:03:27 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-18 18:02:22 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-04-18 18:03:49 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-04-18 18:02:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-04-18 18:04:39 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-18 18:02:10 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.102 |  |
| 2026-04-18 18:00:12 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.121 |  |
| 2026-04-18 18:09:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)