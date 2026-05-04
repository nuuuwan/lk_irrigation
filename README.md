# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_08:23:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,477 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 08:23:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:12:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.013 |  |
| 2026-05-04 08:11:17 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-05-04 08:07:56 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.038 |  |
| 2026-05-04 08:07:19 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.057 |  |
| 2026-05-04 08:06:28 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.078 |  |
| 2026-05-04 08:06:19 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:06:12 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:06:06 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:06:05 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-05-04 08:05:51 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:05:31 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.074 |  |
| 2026-05-04 08:04:55 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.087 |  |
| 2026-05-04 08:04:07 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:04:06 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:03:55 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:03:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-04 08:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-04 08:03:13 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.102 |  |
| 2026-05-04 08:02:52 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-05-04 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:02:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-05-04 08:02:11 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-04 08:02:00 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:01:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:01:47 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:01:47 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-04 08:01:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:01:07 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -5.806 |  |
| 2026-05-04 08:01:00 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-04 08:00:52 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:00:42 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:00:36 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -5.806 |  |
| 2026-05-04 08:00:32 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:00:26 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 07:02:56 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-04 08:03:17 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-04 08:01:00 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-04 06:10:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:01:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:01:47 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:06:19 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 08:00:32 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:04:07 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:23:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:03:55 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:00:26 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:02:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:05:51 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:04:06 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:06:12 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:06:06 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:01:47 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 08:11:17 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-05-04 08:02:11 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-04 08:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-04 08:03:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-04 08:12:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.013 |  |
| 2026-05-04 08:06:05 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-05-04 08:02:52 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-05-04 08:07:56 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.038 |  |
| 2026-05-04 08:01:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:00:52 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:02:00 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.050 |  |
| 2026-05-04 08:07:19 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.057 |  |
| 2026-05-04 08:05:31 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.074 |  |
| 2026-05-04 08:06:28 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.078 |  |
| 2026-05-04 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-05-04 08:04:55 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.087 |  |
| 2026-05-04 08:03:13 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.102 |  |
| 2026-05-04 08:01:07 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -5.806 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)