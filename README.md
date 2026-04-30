# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_21:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 21:13:34 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:11:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.027 |  |
| 2026-04-30 21:10:04 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:07:57 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-04-30 21:07:51 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 21:07:45 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:06:59 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:06:56 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.060 |  |
| 2026-04-30 21:06:28 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 21:06:19 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 21:06:18 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:18 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:05 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:05:51 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:05:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-30 21:05:06 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 21:04:17 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:04:12 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 21:04:10 | Yaka Wewa (Ma Oya) | 1.46 | 🟢 Normal | 0.828 | 🔺 Rising |
| 2026-04-30 21:04:09 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-04-30 21:03:58 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:03:24 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-30 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:03:10 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:02:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-30 21:02:50 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:49 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:31 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:30 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:02:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 21:01:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:01:28 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:00:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:00:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 21:04:10 | Yaka Wewa (Ma Oya) | 1.46 | 🟢 Normal | 0.828 | 🔺 Rising |
| 2026-04-30 21:03:24 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-30 21:02:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 21:02:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-30 21:04:12 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 21:07:51 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 21:06:19 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 21:06:28 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 21:05:06 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 21:03:58 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:00:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:43 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:18 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:03:10 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:10:04 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:00:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:02:30 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:06:05 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:01:28 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:13:34 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 21:07:45 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:50 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:49 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:02:31 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:05:51 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-30 21:04:09 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-04-30 21:05:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-30 21:06:59 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:04:17 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:01:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.022 |  |
| 2026-04-30 21:11:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.027 |  |
| 2026-04-30 21:07:57 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-04-30 21:06:56 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)