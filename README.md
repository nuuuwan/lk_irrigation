# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_04:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 04:09:31 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 04:07:05 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.018 |  |
| 2026-04-07 04:06:23 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:06:02 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-07 04:05:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-07 04:04:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-07 04:03:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-07 04:03:34 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:29 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-04-07 04:03:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.104 |  |
| 2026-04-07 04:02:56 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 04:02:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:33 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-04-07 04:02:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.002 |  |
| 2026-04-07 04:02:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:24 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-07 04:02:06 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |
| 2026-04-07 04:02:00 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:01:49 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:01:41 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:01:31 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-07 04:01:16 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 04:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-04-07 04:01:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:00:35 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-04-07 03:35:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.112 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 03:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-04-07 04:02:24 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-07 03:35:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-07 04:01:16 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 04:05:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-07 04:02:56 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 04:01:31 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-07 04:09:31 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 04:02:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.002 |  |
| 2026-04-07 04:01:41 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:00 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:01:49 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:34 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:06:23 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:33 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:01:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:29 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:02:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-07 03:05:24 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-07 03:04:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-04-07 04:03:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-04-07 04:06:02 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-07 02:08:07 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-04-07 04:07:05 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.018 |  |
| 2026-04-07 03:05:00 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-04-07 04:00:35 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-04-07 04:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-04-07 04:04:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-07 04:02:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-04-07 03:08:26 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.065 |  |
| 2026-04-07 04:02:06 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-07 04:03:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.104 |  |
| 2026-04-07 03:15:19 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)