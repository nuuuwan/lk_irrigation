# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_06:08:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 06:08:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-04-12 06:07:34 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:07:06 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:06:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-04-12 06:06:21 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-12 06:06:12 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:06:04 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 06:06:02 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.056 |  |
| 2026-04-12 06:05:59 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-04-12 06:05:15 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-12 06:04:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:04:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:04:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:57 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:32 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:15 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 06:03:06 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:02:56 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:02:54 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:02:50 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-12 06:02:42 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:02:38 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.059 |  |
| 2026-04-12 06:02:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:02:00 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.034 |  |
| 2026-04-12 06:01:47 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.090 |  |
| 2026-04-12 06:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-12 06:01:36 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -15.216 |  |
| 2026-04-12 06:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-04-12 06:01:17 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.112 |  |
| 2026-04-12 06:01:15 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:01:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.045 |  |
| 2026-04-12 06:01:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-04-12 06:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-04-12 06:00:41 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:00:34 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-12 06:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 05:59:59 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -15.216 |  |
| 2026-04-12 05:51:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | 0.872 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 06:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-04-12 06:02:50 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-12 06:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-12 06:03:15 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 06:06:04 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 06:00:41 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:04:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:07:06 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:04:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:01:15 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:06:12 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:02:56 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:07:34 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:06 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:32 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:57 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:04:12 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:03:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-12 06:08:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-04-12 06:06:21 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-12 06:02:54 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:02:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:02:42 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-12 06:01:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-04-12 06:05:15 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-12 06:00:34 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-12 06:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-04-12 06:06:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-04-12 06:02:00 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.034 |  |
| 2026-04-12 06:01:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.045 |  |
| 2026-04-12 06:06:02 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.056 |  |
| 2026-04-12 06:02:38 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.059 |  |
| 2026-04-12 06:05:59 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-04-12 06:01:47 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.090 |  |
| 2026-04-12 06:01:17 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.112 |  |
| 2026-04-12 06:01:36 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -15.216 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)