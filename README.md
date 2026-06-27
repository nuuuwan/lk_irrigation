# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_11:18:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 11:18:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-27 11:17:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.017 |  |
| 2026-06-27 11:14:54 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:13:22 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 11:11:26 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:09:17 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.036 |  |
| 2026-06-27 11:08:48 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-27 11:07:46 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:07:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-06-27 11:07:10 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.044 |  |
| 2026-06-27 11:07:04 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 11:05:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:05:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:05:04 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:04:52 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:04:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.038 |  |
| 2026-06-27 11:04:07 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-06-27 11:03:42 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-27 11:03:38 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-06-27 11:03:38 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:14 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-27 11:03:13 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.020 |  |
| 2026-06-27 11:03:12 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:53 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 11:02:50 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:43 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-27 11:02:36 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:30 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-27 11:02:24 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:18 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-27 11:02:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 11:02:06 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 11:02:30 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-27 11:08:48 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-27 11:03:42 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-27 11:18:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-27 11:02:18 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-27 11:02:53 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 10:09:31 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 11:07:04 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 11:13:22 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 11:02:06 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:04:52 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:12 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:34 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:50 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:05:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:38 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:01:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:07:46 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:05:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:14:54 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:24 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:11:26 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:02:36 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:11:15 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 11:03:38 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-06-27 11:03:14 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-27 11:02:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 11:02:43 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-27 11:17:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.017 |  |
| 2026-06-27 11:07:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-06-27 11:03:13 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.020 |  |
| 2026-06-27 11:04:07 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-06-27 11:09:17 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.036 |  |
| 2026-06-27 11:04:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.038 |  |
| 2026-06-27 11:07:10 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.044 |  |
| 2026-06-27 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)