# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_07:17:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 07:17:50 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:17:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:14:28 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:13:30 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:08:54 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.135 |  |
| 2026-02-10 07:08:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-10 07:07:31 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:07:10 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.029 |  |
| 2026-02-10 07:06:49 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.077 |  |
| 2026-02-10 07:06:34 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:06:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 07:06:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:06:19 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 07:06:14 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-10 07:05:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-02-10 07:05:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:47 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:43 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 07:04:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-02-10 07:04:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:03:50 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:03:28 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.070 |  |
| 2026-02-10 07:03:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:03:10 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.006 |  |
| 2026-02-10 07:03:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:41 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:04 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:01:53 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.060 |  |
| 2026-02-10 07:01:39 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:01:38 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.011 |  |
| 2026-02-10 07:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:01:16 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-02-10 07:00:18 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-10 06:29:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 06:01:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 07:06:14 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-10 06:03:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-10 07:08:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-10 07:04:43 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 07:06:19 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 07:06:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 07:03:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:17:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:03:50 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:01:39 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:05:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:14:28 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:13:30 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:04 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:47 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:41 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:06:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:04:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:06:48 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:17:50 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:07:31 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:03:10 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.006 |  |
| 2026-02-10 07:03:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:06:34 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:00:18 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-10 07:01:38 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.011 |  |
| 2026-02-10 07:07:10 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.029 |  |
| 2026-02-10 07:01:16 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-02-10 07:04:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-02-10 07:05:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-02-10 07:01:53 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.060 |  |
| 2026-02-10 07:03:28 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.070 |  |
| 2026-02-10 07:06:49 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.077 |  |
| 2026-02-10 07:08:54 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)