# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_04:28:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 04:28:27 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.015 |  |
| 2026-06-27 04:23:17 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-06-27 04:18:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-27 04:13:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:12:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-27 04:11:06 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-06-27 04:08:58 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-06-27 04:08:54 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-06-27 04:06:17 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:06:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-06-27 04:04:59 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:50 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.079 |  |
| 2026-06-27 04:04:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:06 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-27 04:03:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-27 04:02:59 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:51 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:36 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:33 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 04:02:29 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-27 04:02:18 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-27 04:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-06-27 04:01:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 04:01:02 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 04:00:57 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 04:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-06-27 04:02:18 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-27 04:04:06 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-27 04:01:02 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 03:01:24 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 04:01:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 04:02:33 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 03:08:41 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.003 |  |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:59 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:36 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:06:17 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:13:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:13:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:07:14 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:00:57 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:02:51 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:04:59 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:10:50 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:10:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:23:17 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-06-27 04:18:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-27 04:03:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-27 04:28:27 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.015 |  |
| 2026-06-27 04:08:54 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-06-27 04:08:58 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-06-27 04:12:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-27 04:02:29 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-27 04:11:06 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-06-27 04:06:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-06-27 04:04:50 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)