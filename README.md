# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_00:27:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 00:27:33 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.007 |  |
| 2026-01-04 00:22:05 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.013 |  |
| 2026-01-04 00:13:31 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:10:22 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:08:58 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:08:57 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:07:45 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:06:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:06:33 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -1.714 |  |
| 2026-01-04 00:06:12 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -1.714 |  |
| 2026-01-04 00:06:11 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:05:43 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:05:21 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-01-04 00:04:58 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2026-01-04 00:04:55 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 00:04:38 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:04:07 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-04 00:03:59 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 00:03:48 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:03:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 00:03:00 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-04 00:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:02:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:02:28 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-01-04 00:01:58 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:01:52 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:00:57 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:00:40 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-04 00:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 23:59:58 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-01-03 23:35:49 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-04 00:02:28 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-01-03 23:27:01 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-03 23:06:52 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-04 00:00:40 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-04 00:04:07 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-03 23:10:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-04 00:03:59 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 00:04:55 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 00:03:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 00:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 23:06:51 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:02:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:06:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:08:58 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:01:52 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:13:31 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:05:43 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:01:58 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:07:45 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 23:03:19 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:10:22 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:27:33 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.007 |  |
| 2026-01-04 00:04:58 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2026-01-04 00:06:11 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:03:48 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:04:38 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-04 00:00:57 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-03 23:59:58 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-01-03 23:00:29 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-01-04 00:22:05 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.013 |  |
| 2026-01-03 23:02:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-04 00:03:00 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-04 00:05:21 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-04 00:06:33 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)