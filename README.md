# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_18:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,537 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 18:18:24 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.018 |  |
| 2026-06-03 18:09:05 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:08:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:07:59 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:06:27 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:06:25 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 18:06:13 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-06-03 18:06:11 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:06:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.109 |  |
| 2026-06-03 18:05:19 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.009 |  |
| 2026-06-03 18:05:16 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-03 18:05:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:04:26 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:04:09 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:04:03 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:57 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:53 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.013 |  |
| 2026-06-03 18:03:21 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:02:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:02:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-03 18:02:47 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-06-03 18:02:37 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:02:32 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:02:21 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.057 |  |
| 2026-06-03 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-06-03 18:02:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:02:07 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.053 |  |
| 2026-06-03 18:01:57 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:31 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:01:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:53 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:52 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:16 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-03 18:00:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 18:05:16 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-03 18:03:21 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-03 18:00:16 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-03 18:06:25 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 18:06:11 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:04:09 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:02:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:02:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:53 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:53 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:06:27 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:04:03 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:31 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:57 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:08:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:04:26 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:02:32 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:09:05 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:06:13 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-06-03 18:05:19 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.009 |  |
| 2026-06-03 18:05:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:02:37 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:02:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:01:57 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-03 18:02:47 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-06-03 18:03:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.013 |  |
| 2026-06-03 18:18:24 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.018 |  |
| 2026-06-03 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-06-03 18:00:52 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-06-03 18:02:07 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.053 |  |
| 2026-06-03 18:02:21 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.057 |  |
| 2026-06-03 18:06:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)