# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_22:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 22:14:33 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:11:19 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.052 |  |
| 2026-06-10 22:10:11 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:09:51 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-06-10 22:08:36 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:08:15 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 22:07:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:06:26 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:06:21 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:06:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:05:52 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:05:16 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-10 22:05:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:04:37 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.062 |  |
| 2026-06-10 22:04:20 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-06-10 22:04:00 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:03:40 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:03:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:03:17 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:03:11 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-06-10 22:03:08 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-06-10 22:02:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 22:02:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:14 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-06-10 22:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.022 |  |
| 2026-06-10 22:02:11 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-06-10 22:01:39 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 50.400 | 🔺 Rising |
| 2026-06-10 22:01:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 50.400 | 🔺 Rising |
| 2026-06-10 22:01:14 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-06-10 22:01:00 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 22:01:39 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 50.400 | 🔺 Rising |
| 2026-06-10 22:03:08 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-06-10 22:05:16 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-10 22:08:15 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 22:05:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:04:20 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:03:17 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:10:11 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 22:02:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 22:00:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:01:00 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:03:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:14:33 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:06:26 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:07:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:05:52 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:08:36 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:00:49 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:11 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:06:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:04:00 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:03:40 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:06:21 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-10 22:09:51 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-06-10 22:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-06-10 22:03:11 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-06-10 22:02:14 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-10 22:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.022 |  |
| 2026-06-10 22:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-06-10 22:11:19 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.052 |  |
| 2026-06-10 22:04:37 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)