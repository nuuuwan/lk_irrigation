# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_21:18:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 21:18:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-10 21:14:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.077 |  |
| 2026-05-10 21:12:00 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:10:00 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:09:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 21:08:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-10 21:08:34 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:07:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-10 21:07:01 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-10 21:06:53 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-05-10 21:05:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-05-10 21:05:27 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 21:05:14 | Katharagama (Menik Ganga) | 1.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 21:05:14 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-10 21:04:59 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:04:58 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:04:33 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 21:04:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-05-10 21:03:44 | Kuda Oya (Kirindi Oya) | 3.05 | 🟢 Normal | 1.049 | 🔺 Rising |
| 2026-05-10 21:03:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:03:24 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-05-10 21:03:16 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:03:12 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-10 21:02:52 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 21:02:28 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 21:02:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-10 21:02:24 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 21:02:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-10 21:01:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:01:43 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:06 | Wellawaya (Kirindi Oya) | 3.35 | 🟢 Normal | 1.517 | 🔺 Rising |
| 2026-05-10 21:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-05-10 21:00:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:00:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 21:01:06 | Wellawaya (Kirindi Oya) | 3.35 | 🟢 Normal | 1.517 | 🔺 Rising |
| 2026-05-10 21:03:44 | Kuda Oya (Kirindi Oya) | 3.05 | 🟢 Normal | 1.049 | 🔺 Rising |
| 2026-05-10 21:08:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-10 21:07:01 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-10 21:03:24 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-05-10 21:05:14 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-10 21:03:12 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-10 21:02:28 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 21:00:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 21:02:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-10 21:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 21:05:14 | Katharagama (Menik Ganga) | 1.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 21:02:24 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 21:09:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 21:05:27 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 21:04:33 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 21:18:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:04:59 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:03:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:10:00 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:43 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:02:52 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:04:58 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:08:34 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:03:16 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:00:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-05-10 21:04:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 21:02:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-10 21:07:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-10 21:05:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-05-10 21:12:00 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:01:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:06:53 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-05-10 21:14:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)