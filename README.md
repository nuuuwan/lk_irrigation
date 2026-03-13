# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_01:52:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 01:52:39 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.017 |  |
| 2026-03-14 01:28:00 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.007 |  |
| 2026-03-14 01:26:24 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 01:07:43 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 01:06:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.219 |  |
| 2026-03-14 01:06:03 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:05:55 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:05:39 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 01:05:18 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 01:04:32 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 01:03:52 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:31 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:21 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-03-14 01:03:16 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-14 01:03:07 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-03-14 01:02:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:45 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.150 |  |
| 2026-03-14 01:02:34 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:28 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-14 01:02:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 01:02:09 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:08 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:51 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:19 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-14 01:01:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 00:03:41 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-14 01:03:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-14 01:01:19 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-14 00:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-14 01:05:39 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 01:05:18 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 01:07:43 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 01:02:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 01:26:24 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 01:04:32 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 01:02:34 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:21 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:07:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:05:55 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:19:04 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:31 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:52 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:16 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:02:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:09 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:51 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:06:03 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:27:36 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.007 |  |
| 2026-03-14 01:28:00 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.007 |  |
| 2026-03-14 01:01:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-14 01:52:39 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.017 |  |
| 2026-03-14 01:02:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-14 01:03:07 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-03-14 01:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 01:02:45 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.150 |  |
| 2026-03-14 01:06:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.219 |  |
| 2026-03-14 00:10:22 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)