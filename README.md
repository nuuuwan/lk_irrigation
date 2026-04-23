# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_01:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 01:13:08 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.044 |  |
| 2026-04-24 01:12:29 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-24 01:10:08 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-24 01:07:39 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.161 |  |
| 2026-04-24 01:07:26 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-24 01:07:05 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:07:00 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:06:48 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 01:05:28 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:05:26 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-04-24 01:04:57 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 01:04:51 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:03:56 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 01:03:46 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.039 |  |
| 2026-04-24 01:03:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-04-24 01:02:56 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:02:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 01:02:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-24 01:02:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-24 01:02:00 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-24 01:01:50 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-04-24 01:01:49 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.036 |  |
| 2026-04-24 01:01:06 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:00:59 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-24 01:00:35 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:00:26 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.050 |  |
| 2026-04-24 01:00:18 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.080 |  |
| 2026-04-24 01:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-24 00:48:19 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 01:07:26 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-24 01:10:08 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-24 00:06:28 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-24 01:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-24 01:02:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-24 01:02:00 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-24 01:04:57 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 01:02:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:07:05 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 01:06:48 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 01:05:28 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:17:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:00:35 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:04:51 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:07:05 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:02:56 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:02:26 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:01:06 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:07:00 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:03:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-04-24 01:12:29 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-24 01:03:56 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 00:14:52 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-04-24 00:07:54 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-04-24 01:05:26 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-04-24 01:00:59 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-24 01:02:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-24 01:01:50 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-04-24 01:01:49 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.036 |  |
| 2026-04-24 01:03:46 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.039 |  |
| 2026-04-24 01:13:08 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.044 |  |
| 2026-04-24 00:06:57 | Kuda Oya (Kirindi Oya) | 2.40 | 🟢 Normal | -0.046 |  |
| 2026-04-24 01:00:26 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.050 |  |
| 2026-04-24 00:17:42 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.071 |  |
| 2026-04-24 01:00:18 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.080 |  |
| 2026-04-24 01:07:39 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)