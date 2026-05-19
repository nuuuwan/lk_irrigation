# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_14:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 14:10:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.077 |  |
| 2026-05-19 14:10:26 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-05-19 14:08:07 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:52 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:40 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:09 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:05:38 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:05:34 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:05:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-19 14:05:08 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:04:48 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-19 14:04:17 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-05-19 14:03:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-19 14:03:21 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-19 14:03:20 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:10 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:03:10 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:04 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-05-19 14:02:56 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:02:50 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:50 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-19 14:02:41 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:02:31 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:11 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 14:02:09 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:01:59 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 14:01:58 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.022 |  |
| 2026-05-19 14:01:56 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-19 14:01:50 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:50 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -2.250 |  |
| 2026-05-19 14:01:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:34 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -2.250 |  |
| 2026-05-19 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:31 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.090 |  |
| 2026-05-19 14:01:21 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 14:00:22 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 14:05:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-19 14:03:21 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-19 14:01:56 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-19 14:02:50 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-19 14:03:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-19 14:01:21 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 14:00:22 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:50 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:50 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:31 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:20 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:08:07 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:31 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:52 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:01:32 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:05:34 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:03:10 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:40 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:06:09 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:02:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 14:04:48 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-19 14:01:59 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 14:02:11 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 14:03:10 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:02:09 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:02:41 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-05-19 14:03:04 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-05-19 14:10:26 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-05-19 14:04:17 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-05-19 14:02:56 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:05:08 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:05:38 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.020 |  |
| 2026-05-19 14:01:58 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.022 |  |
| 2026-05-19 14:10:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.077 |  |
| 2026-05-19 14:01:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.090 |  |
| 2026-05-19 14:01:50 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)