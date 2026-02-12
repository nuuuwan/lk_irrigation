# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_11:49:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,986 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 11:49:10 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:28:37 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 11:19:49 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:14:26 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:10:34 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:44 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-12 11:07:14 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-12 11:07:11 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 11:06:03 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-12 11:05:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:05:34 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.080 |  |
| 2026-02-12 11:05:27 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.078 |  |
| 2026-02-12 11:05:21 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:05:09 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:28 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:12 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:11 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-12 11:04:11 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:02 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:03:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-12 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-02-12 11:03:24 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-02-12 11:03:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:02:30 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:02:26 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:01:56 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 11:01:54 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-12 11:01:31 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:01:31 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:01:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:00:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:00:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:00:41 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:00:30 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:00:18 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 11:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-02-12 11:04:11 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-12 11:01:56 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 11:28:37 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 11:07:11 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 11:01:31 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:10:34 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:01:31 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:14:26 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:03:24 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:00:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:05:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:01:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:05:09 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:11 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:12 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:05:21 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:49:10 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:02 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:04:28 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:00:30 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:19:49 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:02:26 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:44 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:02:30 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 11:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-12 11:06:03 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-12 11:03:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-12 11:00:41 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:00:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:03:16 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-02-12 11:07:14 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-12 11:01:54 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-12 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-02-12 11:00:18 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-02-12 11:05:27 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.078 |  |
| 2026-02-12 11:05:34 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)