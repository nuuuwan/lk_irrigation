# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_11:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 11:14:30 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-07-04 11:13:10 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:10:32 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-04 11:09:03 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:08:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.042 |  |
| 2026-07-04 11:08:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:07:49 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.100 |  |
| 2026-07-04 11:06:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 11:06:20 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 11:06:15 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 11:05:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:05:50 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 11:05:46 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 11:04:05 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:03:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:03:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:03:38 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 11:03:30 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 11:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:02:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 11:02:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:02:20 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-07-04 11:02:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:02:07 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.088 |  |
| 2026-07-04 11:02:06 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 11:02:06 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.314 |  |
| 2026-07-04 11:02:03 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 11:01:35 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:01:35 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-07-04 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:01:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:01:00 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-07-04 11:00:54 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:00:52 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:00:49 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-07-04 11:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 10:22:41 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-07-04 11:14:30 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-07-04 11:03:30 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 11:06:20 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 11:06:15 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 11:10:32 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-04 11:02:03 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 11:05:50 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 11:03:38 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 11:02:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 11:02:06 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 11:06:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 11:05:46 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 11:02:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:03:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:02:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:13:10 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:04:05 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:09:03 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 10:00:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:03:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:05:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:00:54 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:01:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:01:35 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:08:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-04 10:02:52 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:00:52 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 11:00:49 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-07-04 11:01:00 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-07-04 11:01:35 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-07-04 11:02:20 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-07-04 11:08:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.042 |  |
| 2026-07-04 11:02:07 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.088 |  |
| 2026-07-04 11:07:49 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.100 |  |
| 2026-07-04 11:02:06 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.314 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)