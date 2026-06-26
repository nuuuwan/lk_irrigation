# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_01:37:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,334 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 01:37:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:36:42 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-06-27 01:17:19 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.049 |  |
| 2026-06-27 01:10:09 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:09:56 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-27 01:08:33 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-27 01:06:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:19 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-27 01:05:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:05:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:05:15 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-06-27 01:04:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 01:04:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:04:02 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.038 |  |
| 2026-06-27 01:04:00 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-06-27 01:03:36 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:03:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:46 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-27 01:02:45 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.126 |  |
| 2026-06-27 01:02:22 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:19 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 01:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:01:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:00:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.385 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 01:00:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-06-27 01:08:33 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-27 01:02:46 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-27 01:01:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-27 01:09:56 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-27 01:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-27 01:04:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 22:07:10 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 01:01:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 01:05:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:37:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:20:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:03:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:10:09 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:04:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:17:19 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:44:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:19 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:05:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:07:58 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:06:19 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:22 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:03:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:36:42 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-06-27 01:03:36 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:02:45 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:05:15 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-06-27 01:04:02 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.038 |  |
| 2026-06-27 01:04:00 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-06-27 01:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.049 |  |
| 2026-06-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)