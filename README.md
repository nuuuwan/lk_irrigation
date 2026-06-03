# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_14:20:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,380 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 14:20:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.008 |  |
| 2026-06-03 14:17:52 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.017 |  |
| 2026-06-03 14:12:45 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-06-03 14:09:09 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:08:59 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:08:18 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 14:08:03 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:07:18 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 14:07:06 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:06:57 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 14:06:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 14:06:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:06:04 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:05:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-03 14:05:04 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:05:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:04:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 14:04:39 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-03 14:04:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:03:40 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:39 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-06-03 14:03:38 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:23 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:13 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-03 14:03:00 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:02:48 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:44 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:37 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-06-03 14:01:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-06-03 14:01:19 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-06-03 14:01:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:00:55 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:00:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:00:38 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-03 14:00:22 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-03 13:59:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 14:04:39 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-03 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-06-03 14:03:13 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-03 14:05:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-03 14:08:18 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 14:06:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 14:04:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 14:00:55 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:02:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:08:03 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:04:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 14:07:18 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 14:06:57 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 13:01:31 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:00:22 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:01:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:05:04 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:09:09 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:07:06 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:00 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:05:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:40 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:06:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:06:04 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:03:23 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 14:20:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.77 | 🟢 Normal | -0.008 |  |
| 2026-06-03 14:01:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-06-03 14:08:59 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:48 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:44 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:00:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:02:37 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-03 14:03:39 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-06-03 14:12:45 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-06-03 14:17:52 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.017 |  |
| 2026-06-03 14:00:38 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-03 14:01:19 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)