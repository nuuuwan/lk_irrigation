# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_16:15:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 16:15:39 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-01 16:08:35 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:08:33 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-01 16:08:20 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:06:13 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:05:59 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:05:52 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:05:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:05:12 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:04:55 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:19 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:16 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:06 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:03:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 16:03:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:03:30 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:03:27 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.081 |  |
| 2026-06-01 16:03:16 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.040 |  |
| 2026-06-01 16:03:09 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-01 16:03:08 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.059 |  |
| 2026-06-01 16:02:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:02:36 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-01 16:02:34 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-01 16:02:25 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:02:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:01:57 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 16:01:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:01:30 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:01:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-06-01 16:00:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:00:35 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-01 16:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:00:16 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 16:02:36 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-01 16:15:39 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-01 16:03:09 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-01 16:00:35 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-01 16:01:57 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 16:03:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 15:03:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 16:04:19 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:01:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 15:01:27 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:00:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:05:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:02:25 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:03:30 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:02:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:06 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:03:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:06:13 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:08:20 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:00:16 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:05:52 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 15:04:11 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:55 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:04:16 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 16:08:33 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-01 16:08:35 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:05:59 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:03:08 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:01:30 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:02:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-01 15:02:56 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:05:12 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-01 16:02:34 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-01 16:01:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-06-01 16:03:16 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.040 |  |
| 2026-06-01 16:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.059 |  |
| 2026-06-01 16:03:27 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)