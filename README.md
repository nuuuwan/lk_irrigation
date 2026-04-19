# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_18:11:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 18:11:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.112 |  |
| 2026-04-19 18:09:14 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:06:00 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-04-19 18:05:54 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:05:50 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 18:05:42 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.046 |  |
| 2026-04-19 18:05:09 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:05:01 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:04:28 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:04:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:04:02 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:04:02 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-19 18:03:58 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:03:56 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-19 18:03:45 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2026-04-19 18:03:32 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 18:03:21 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 18:03:09 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:03:07 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-04-19 18:03:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-19 18:03:03 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:46 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-19 18:02:28 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:28 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-19 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:02:13 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 18:02:07 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:00 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.085 |  |
| 2026-04-19 18:01:29 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:12 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-19 18:01:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-19 17:31:07 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:31:00 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 18:02:07 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-04-19 18:02:46 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-19 18:04:02 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-19 18:03:56 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-19 17:07:14 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-19 18:03:32 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 18:03:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-19 18:02:13 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 18:03:21 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 18:05:50 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 18:01:29 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:04:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:03:58 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:03:09 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:03:03 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:04:02 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:05:09 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:28 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:09:14 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:05:54 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:01:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:00 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:06:00 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-04-19 18:02:28 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-19 18:01:12 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-19 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:05:01 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:04:28 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-19 18:03:45 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2026-04-19 18:03:07 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-04-19 18:05:42 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.046 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-19 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.085 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 18:11:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)