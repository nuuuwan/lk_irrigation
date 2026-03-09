# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_10:22:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,351 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 10:22:25 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:22:24 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.046 |  |
| 2026-03-09 10:16:27 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:12:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:11:30 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:09:13 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-03-09 10:08:11 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.120 |  |
| 2026-03-09 10:07:04 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-03-09 10:06:04 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-03-09 10:05:46 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:15 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:12 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:04:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:03:45 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:03:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:03:32 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 10:03:32 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 10:03:23 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:03:22 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.131 |  |
| 2026-03-09 10:02:54 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:52 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-03-09 10:02:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-03-09 10:02:26 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:26 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:17 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-03-09 10:02:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-03-09 10:01:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-09 10:01:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:01:40 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 10:01:30 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:01:23 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:01:00 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:00:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.053 |  |
| 2026-03-09 10:00:31 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:00:22 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 10:02:52 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-03-09 10:02:17 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-03-09 10:01:40 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 10:03:32 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 10:03:32 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 10:01:23 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 10:02:26 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:00:22 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:26 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:01:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:46 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:03:23 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:54 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:22:25 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:00:31 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:01:30 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:15 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:11:30 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:03:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:02:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:04:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:01:00 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:12:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-09 10:05:12 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:03:45 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-09 10:02:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-03-09 10:01:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-09 10:07:04 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-03-09 10:09:13 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-03-09 10:06:04 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-03-09 10:22:24 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.046 |  |
| 2026-03-09 10:00:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.053 |  |
| 2026-03-09 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-03-09 10:08:11 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.120 |  |
| 2026-03-09 10:03:22 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)