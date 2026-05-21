# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_10:25:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,767 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 10:25:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.022 |  |
| 2026-05-21 10:21:27 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-05-21 10:11:29 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-05-21 10:10:37 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:08:06 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:07:15 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:06:44 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:06:39 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:06:30 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.019 |  |
| 2026-05-21 10:06:02 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.041 |  |
| 2026-05-21 10:06:02 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-05-21 10:06:00 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.057 |  |
| 2026-05-21 10:05:53 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:04:17 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:04:16 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:04:03 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 10:03:43 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-21 10:03:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:03:34 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:03:34 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:03:32 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:03:00 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:02:59 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:48 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.112 |  |
| 2026-05-21 10:02:38 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-21 10:02:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:22 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-21 10:02:19 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:01:57 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-05-21 10:01:42 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:01:14 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:00:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 10:00:26 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:00:20 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:00:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-21 10:02:22 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-21 10:00:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 10:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 10:00:26 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:19 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:38 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:59 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:04:16 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:06:39 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:07:15 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:00:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:03:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:02:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:05:53 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:04:17 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:08:06 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:10:37 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:01:14 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:01:42 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 10:21:27 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-05-21 10:11:29 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-05-21 10:06:44 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:03:32 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:03:00 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:04:03 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-21 10:01:57 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-05-21 10:06:30 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.019 |  |
| 2026-05-21 10:06:02 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-05-21 10:03:34 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:00:20 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-05-21 10:25:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.022 |  |
| 2026-05-21 10:03:43 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-21 10:06:02 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.041 |  |
| 2026-05-21 10:06:00 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.057 |  |
| 2026-05-21 10:02:48 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)