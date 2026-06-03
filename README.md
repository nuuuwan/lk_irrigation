# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_04:30:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 04:30:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:15:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-04 04:08:06 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:06:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 04:06:00 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-04 04:05:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-04 04:04:53 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:41 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:38 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-04 04:04:19 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 04:04:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 04:04:15 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 04:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-04 04:04:06 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:00 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.100 |  |
| 2026-06-04 04:03:32 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:03:29 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 04:03:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:03:10 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:02:33 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 04:02:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 04:02:07 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-04 04:02:02 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:39 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.091 |  |
| 2026-06-04 04:01:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:10 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:00:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 03:47:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 03:02:53 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | 1.403 | 🔺 Rising |
| 2026-06-04 03:56:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 04:04:38 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-04 04:02:33 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 04:02:07 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-04 04:06:00 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-04 04:06:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 04:04:19 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 03:04:31 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 04:15:19 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-04 03:03:39 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 04:02:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 04:04:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 04:04:15 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 04:03:29 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:00:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:10 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:03:32 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:02:02 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:05:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:53 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:03:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:06 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:41 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:08:06 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:39 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:03:10 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:30:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-04 04:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-04 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.091 |  |
| 2026-06-04 04:04:00 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)