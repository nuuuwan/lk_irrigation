# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_04:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,614 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 04:06:25 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-04 04:06:20 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-04 04:06:17 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:06:01 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:04:50 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:47 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-03-04 04:04:21 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:17 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:00 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:03:41 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-04 04:03:30 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:03:05 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 04:03:02 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:02:50 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:02:23 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:02:14 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-03-04 04:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-04 04:02:05 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 04:02:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-04 04:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:36 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:06 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:00 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:00:38 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-04 03:59:22 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.204 |  |
| 2026-03-04 03:57:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-04 03:40:16 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-04 03:29:31 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 03:08:33 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-04 02:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-04 04:00:38 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-04 04:06:25 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-04 04:02:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-04 03:57:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-04 04:02:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-04 04:06:20 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-04 04:03:05 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 04:02:05 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-04 04:03:41 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-04 04:02:50 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:50 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:03:02 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-04 03:03:05 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:06 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 03:11:05 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:21 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:03:30 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-04 03:29:31 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 02:01:33 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:04:17 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:36 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:06:17 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:01:00 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-04 03:06:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-04 02:05:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 04:06:01 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:04:00 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-04 02:01:28 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:02:23 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-04 04:04:47 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-03-04 04:02:14 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-03-04 03:59:22 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)