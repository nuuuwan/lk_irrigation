# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_06:32:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,406 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 06:32:36 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:25:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:14:34 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.035 |  |
| 2026-06-28 06:10:23 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-28 06:09:07 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-06-28 06:08:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.005 |  |
| 2026-06-28 06:07:20 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:07:17 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:06:39 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:06:19 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-06-28 06:06:12 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.164 |  |
| 2026-06-28 06:05:16 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-06-28 06:05:12 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:05:12 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-06-28 06:05:00 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:04:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:04:31 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:41 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.092 |  |
| 2026-06-28 06:03:14 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.052 |  |
| 2026-06-28 06:03:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:02 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:50 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 06:02:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-06-28 06:02:25 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:20 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 06:05:12 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-06-28 06:00:29 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 06:02:50 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 06:10:23 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-28 06:01:16 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 06:08:03 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.005 |  |
| 2026-06-28 06:07:17 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:02 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:25:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:32:36 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:04:31 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:01:27 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:10 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:02:20 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:00:45 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:41 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:01:43 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:03:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:04:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:07:20 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:06:39 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:05:12 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-06-28 06:02:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-06-28 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-28 06:01:14 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.017 |  |
| 2026-06-28 06:06:19 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-06-28 06:05:16 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-06-28 06:01:37 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.034 |  |
| 2026-06-28 06:14:34 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.035 |  |
| 2026-06-28 06:03:14 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.052 |  |
| 2026-06-28 06:09:07 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-06-28 06:02:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.061 |  |
| 2026-06-28 06:03:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.092 |  |
| 2026-06-28 06:06:12 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.164 |  |
| 2026-06-28 06:01:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.434 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)