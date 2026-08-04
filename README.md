# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_08:05:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,502 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 08:05:52 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.095 |  |
| 2026-08-04 08:05:29 | Nawalapitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 08:05:14 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | -0.266 |  |
| 2026-08-04 08:05:08 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.272 |  |
| 2026-08-04 08:04:32 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:04:27 | Kithulgala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:04:24 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.041 |  |
| 2026-08-04 08:04:12 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-08-04 08:04:00 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | -0.090 |  |
| 2026-08-04 08:03:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:03:43 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:03:15 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-04 08:03:05 | Peradeniya (Mahaweli Ganga) | 4.85 | 🟢 Normal | -0.130 |  |
| 2026-08-04 08:02:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:43 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.061 |  |
| 2026-08-04 08:02:42 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-08-04 08:02:33 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-08-04 08:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | 0.000 |  |
| 2026-08-04 08:02:20 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:03 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:03 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-08-04 08:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:01:34 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 08:01:14 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-04 08:01:13 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:00:39 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:00:32 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:41:38 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:34:40 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 08:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | 0.000 |  |
| 2026-08-04 07:06:09 | Rathnapura (Kalu Ganga) | 7.33 | 🟡 Alert | -0.083 |  |
| 2026-08-04 08:02:42 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-08-04 07:02:16 | Putupaula (Kalu Ganga) | 1.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-04 08:01:14 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-04 07:06:18 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-04 08:05:29 | Nawalapitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 07:00:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 08:01:34 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 08:04:27 | Kithulgala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:20 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:04:32 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:01:42 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:00:32 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:05:49 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:00:39 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:03:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:03 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:01:13 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:03:43 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-04 07:02:35 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 08:02:03 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-08-04 08:03:15 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-08-04 07:05:46 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-08-04 07:00:17 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.020 |  |
| 2026-08-04 07:01:08 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-08-04 08:04:24 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.041 |  |
| 2026-08-04 08:04:12 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-08-04 08:02:33 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-08-04 07:34:40 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.049 |  |
| 2026-08-04 08:02:43 | Nagalagam Street (Kelani Ganga) | 1.19 | 🟢 Normal | -0.061 |  |
| 2026-08-04 08:04:00 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | -0.090 |  |
| 2026-08-04 08:05:52 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.095 |  |
| 2026-08-04 07:02:28 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.101 |  |
| 2026-08-04 08:03:05 | Peradeniya (Mahaweli Ganga) | 4.85 | 🟢 Normal | -0.130 |  |
| 2026-08-04 08:05:14 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | -0.266 |  |
| 2026-08-04 08:05:08 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)