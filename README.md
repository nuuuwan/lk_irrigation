# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_21:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 21:12:47 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.017 |  |
| 2026-06-04 21:12:12 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:08:11 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:07:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:06:58 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.035 |  |
| 2026-06-04 21:06:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.131 |  |
| 2026-06-04 21:06:41 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:06:20 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 21:05:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-04 21:05:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 21:04:52 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-06-04 21:04:47 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 21:04:46 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.045 |  |
| 2026-06-04 21:04:38 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-06-04 21:04:34 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-04 21:04:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:29 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:26 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:20 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 21:03:27 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 21:03:25 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 21:03:18 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.200 |  |
| 2026-06-04 21:03:17 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:03:00 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:03:00 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-04 21:02:29 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:28 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 21:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-04 21:02:17 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 21:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:02 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.049 |  |
| 2026-06-04 21:02:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:01:32 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:00:44 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.101 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 21:04:34 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-04 20:05:11 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-04 21:04:20 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 21:03:00 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-04 21:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-04 21:02:17 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 21:05:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-04 21:06:20 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 21:03:25 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 21:04:47 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 21:03:27 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 21:05:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 21:04:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:07:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:03:17 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:06:41 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:29 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:12:12 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:04:26 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:03:00 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:01:32 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:08:11 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:28 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 21:12:47 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.017 |  |
| 2026-06-04 21:04:52 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-06-04 21:06:58 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.035 |  |
| 2026-06-04 21:04:38 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-06-04 21:04:46 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.045 |  |
| 2026-06-04 21:02:02 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.049 |  |
| 2026-06-04 21:00:44 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.101 |  |
| 2026-06-04 21:06:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.131 |  |
| 2026-06-04 21:03:18 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)