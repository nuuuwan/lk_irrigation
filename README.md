# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_22:26:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,559 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 22:26:08 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:08:36 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:07:10 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:07:05 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-05-18 22:06:58 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:06:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 22:06:36 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:06:34 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.127 |  |
| 2026-05-18 22:06:12 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:05:35 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:05:34 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-05-18 22:05:21 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:05:05 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-05-18 22:04:34 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.023 |  |
| 2026-05-18 22:04:29 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-05-18 22:04:29 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:04:26 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:04:17 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:49 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 22:03:44 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:03:32 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:24 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:23 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:15 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:13 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 22:02:15 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-18 22:01:57 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-05-18 22:01:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:01:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:01:21 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:01:21 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-18 22:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:09 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 21:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-05-18 22:01:21 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-18 22:03:13 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 22:03:49 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 22:06:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 22:06:36 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:09 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:26:08 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:01:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:15 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:51:29 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:04:26 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:00:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:24 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:07:10 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:08:36 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:03:32 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:04:17 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:02:15 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 22:07:05 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-05-18 22:05:05 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-05-18 22:05:21 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:01:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:06:58 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:01:21 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-18 22:01:57 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-05-18 22:06:12 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:05:35 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:03:44 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-05-18 22:05:34 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-05-18 22:04:34 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.023 |  |
| 2026-05-18 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-18 22:04:29 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-18 22:06:34 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)