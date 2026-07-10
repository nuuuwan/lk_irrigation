# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_19:26:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,681 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 19:26:12 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.043 |  |
| 2026-07-10 19:22:13 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:12:14 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 19:09:54 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-10 19:09:44 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-10 19:09:41 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-10 19:07:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:06:41 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-10 19:06:15 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-10 19:05:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:05:01 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 19:04:44 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:59 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 19:03:55 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-10 19:03:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 19:03:29 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:23 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-10 19:03:12 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-07-10 19:02:48 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-10 19:02:17 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:12 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 19:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:00 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:01:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 19:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-07-10 19:00:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-10 19:00:44 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 19:06:15 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-10 19:03:55 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-10 19:09:44 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-10 19:09:54 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-10 19:09:41 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-10 19:06:41 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-10 19:02:12 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 19:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 19:05:01 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 19:03:59 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 19:03:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 19:12:14 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 19:03:23 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:01:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:44 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:05:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:00:44 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:04:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:17 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:48 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:12 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:02:00 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:22:13 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:07:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:03:29 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 19:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-07-10 19:02:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-10 19:00:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-10 19:03:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-07-10 19:26:12 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)