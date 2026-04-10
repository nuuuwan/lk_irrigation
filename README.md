# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_18:13:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,496 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:13:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:13:40 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:09:53 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:09:37 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-10 18:07:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:06:35 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 18:06:26 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 18:06:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-10 18:06:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-10 18:06:00 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-10 18:04:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:44 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:30 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-10 18:04:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:19 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:04:10 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-04-10 18:03:53 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-10 18:03:41 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:03:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:02:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 18:02:53 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:02:48 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:46 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:36 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:34 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-04-10 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 18:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-10 18:01:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:23 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:00:49 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 18:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-10 18:03:53 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-10 18:01:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-10 18:06:00 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-10 18:09:37 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-10 18:06:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-10 18:06:35 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 18:04:30 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-10 18:01:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:03:41 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:04:19 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 18:02:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 18:00:49 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 18:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 18:06:26 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 18:01:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:07:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:46 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:13:40 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:44 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:03:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:06:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:36 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:13:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:09:53 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:04:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:48 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:23 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:02:53 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:04:10 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-04-10 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 18:02:34 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)