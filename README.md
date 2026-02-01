# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_05:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 05:05:34 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:05:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 05:05:14 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 05:04:59 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-02 05:04:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:04:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:51 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 05:03:21 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-02 05:02:58 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:02:58 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-02 05:02:55 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 05:02:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:02:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-02 05:02:23 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.255 |  |
| 2026-02-02 05:02:21 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-02 05:02:10 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:01:21 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:01:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-02-02 05:01:05 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 05:00:51 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:49 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:48 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:47 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:47 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:00:46 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:44 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 05:00:43 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 04:27:55 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.007 |  |
| 2026-02-02 04:20:09 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.024 |  |
| 2026-02-02 04:18:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 05:00:51 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-02 03:04:09 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-02 04:06:55 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-02 05:02:21 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-02 05:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-02 05:01:05 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 05:03:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 05:05:14 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 05:05:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 05:04:59 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-02 05:02:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:21 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:02:10 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:51 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-02 04:02:27 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-02 04:05:07 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:05:34 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 04:04:04 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:03:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 04:01:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:04:11 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:04:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:00:47 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:01:21 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:01:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-02-02 04:27:55 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.007 |  |
| 2026-02-02 05:02:55 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 05:02:58 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-02 05:02:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-02 04:20:09 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.024 |  |
| 2026-02-02 04:07:05 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.029 |  |
| 2026-02-02 04:01:02 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.031 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-02 04:09:09 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.056 |  |
| 2026-02-02 04:08:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.126 |  |
| 2026-02-02 05:02:23 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.255 |  |
| 2026-02-02 04:04:21 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.383 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)