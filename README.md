# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_04:08:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 04:08:32 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:05:57 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:05:46 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:04:46 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.080 |  |
| 2026-06-06 04:04:32 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-06 04:04:22 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-06 04:04:11 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.070 |  |
| 2026-06-06 04:03:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-06 04:03:57 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:03:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:03:30 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.027 |  |
| 2026-06-06 04:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:49 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 04:02:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:46 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-06-06 04:02:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:28 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:07 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:51 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:34 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:01:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:21 | Ellagawa (Kalu Ganga) | 7.17 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-06 04:01:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:12 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:00:58 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2026-06-06 03:39:44 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-06-06 03:28:02 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-06-06 03:19:32 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.027 |  |
| 2026-06-06 03:19:31 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 04:04:32 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-06 03:39:44 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-06-06 04:04:22 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-06 04:01:21 | Ellagawa (Kalu Ganga) | 7.17 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-06 04:03:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-06 04:02:49 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 04:01:51 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 03:03:00 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:34 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 03:05:17 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:01:12 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:08:32 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 03:07:34 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:05:57 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:28 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 03:02:29 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:07 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:03:57 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:05:46 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:01:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-06 04:03:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-06 03:05:14 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-06 04:02:46 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-06-06 04:03:30 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.027 |  |
| 2026-06-06 04:00:58 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2026-06-06 03:08:41 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.031 |  |
| 2026-06-06 03:11:40 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.070 |  |
| 2026-06-06 04:04:11 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.070 |  |
| 2026-06-06 04:04:46 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.080 |  |
| 2026-06-06 03:09:05 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)