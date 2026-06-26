# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_12:05:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 12:05:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:05:34 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-06-26 12:05:33 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:31 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-26 12:04:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:04 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 12:03:52 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-26 12:03:43 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.019 |  |
| 2026-06-26 12:03:43 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-26 12:03:43 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-26 12:03:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 12:03:15 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 12:03:04 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:51 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:23 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-26 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.084 |  |
| 2026-06-26 12:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:56 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 12:01:44 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-26 12:01:29 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.011 |  |
| 2026-06-26 12:01:23 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:17 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:15 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:14 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.011 |  |
| 2026-06-26 12:01:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:00:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:46:39 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:14:35 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.025 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 12:03:52 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-26 12:01:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 12:03:43 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-26 12:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 11:14:35 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-26 12:02:23 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-26 12:04:04 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 12:03:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 12:04:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:15 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:00:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:23 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:05:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:51 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:00:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:05:33 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:09:34 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:17 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:03:15 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:03:04 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:07:08 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:01:11 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:04:31 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-26 11:04:26 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:01:56 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-26 12:03:43 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-26 12:01:44 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-26 11:04:30 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-06-26 12:01:14 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.011 |  |
| 2026-06-26 12:01:29 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.011 |  |
| 2026-06-26 12:03:43 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.019 |  |
| 2026-06-26 12:04:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-26 12:05:34 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-06-26 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.084 |  |
| 2026-06-26 11:04:43 | Glencourse (Kelani Ganga) | 6.85 | 🟢 Normal | -3.131 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)