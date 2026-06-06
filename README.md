# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_07:36:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,799 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 07:36:15 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.128 |  |
| 2026-06-06 07:20:44 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:14:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-06 07:13:43 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:12:31 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:11:13 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-06-06 07:10:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:10:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:08:41 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-06 07:08:30 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:07:51 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.046 |  |
| 2026-06-06 07:06:38 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-06 07:05:52 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | -0.080 |  |
| 2026-06-06 07:05:31 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 07:05:10 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:05:04 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:04:56 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:55 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 07:04:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:17 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:03:48 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:03:36 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:03:27 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 07:03:26 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 07:03:25 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.010 |  |
| 2026-06-06 07:03:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:03:23 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-06 07:02:46 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 07:02:28 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-06 07:02:23 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:02:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 07:02:08 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:02:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:01:46 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.138 |  |
| 2026-06-06 07:01:12 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.002 |  |
| 2026-06-06 07:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:01:02 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-06-06 07:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:00:44 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:00:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 07:03:25 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.010 |  |
| 2026-06-06 07:03:27 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 07:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-06 07:06:38 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-06 07:08:41 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-06 07:02:28 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-06 07:04:55 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 07:02:46 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 07:00:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-06 07:02:08 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:05:04 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 07:14:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-06 07:02:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 07:05:31 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 07:01:12 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.002 |  |
| 2026-06-06 07:00:44 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:02:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:03:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:13:43 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:03:23 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:10:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:10:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:20:44 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:04:56 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 07:11:13 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-06-06 07:08:30 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:03:36 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:02:23 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:04:17 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:03:48 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-06 07:07:51 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.046 |  |
| 2026-06-06 07:01:02 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-06-06 07:05:52 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | -0.080 |  |
| 2026-06-06 07:36:15 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.128 |  |
| 2026-06-06 07:01:46 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)