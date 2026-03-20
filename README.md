# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_19:42:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 19:42:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.036 |  |
| 2026-03-20 19:36:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.063 |  |
| 2026-03-20 19:17:06 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.025 |  |
| 2026-03-20 19:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:13:50 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.017 |  |
| 2026-03-20 19:11:19 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 19:09:58 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:09:47 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:09:24 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:06:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-20 19:05:48 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:05:27 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.029 |  |
| 2026-03-20 19:05:15 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-20 19:04:43 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:04:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 19:03:53 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:03:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:03:33 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:03:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.187 |  |
| 2026-03-20 19:03:21 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.051 |  |
| 2026-03-20 19:02:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:02:55 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 19:02:39 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:02:25 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 19:02:23 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:02:09 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:02:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:52 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:47 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-03-20 19:01:26 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:24 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:01:22 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:01:20 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-03-20 19:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:00:52 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:00:22 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 19:01:20 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-03-20 19:01:47 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-03-20 19:06:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-20 19:02:55 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 19:02:25 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 19:04:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 19:11:19 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 19:01:26 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:09:24 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:00:52 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:02:39 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:09:58 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:02:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:09:47 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:05:48 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:03:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:01:52 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:02:09 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 19:03:53 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:03:33 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:04:43 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:01:22 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:02:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:02:23 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:01:24 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-20 19:13:50 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.017 |  |
| 2026-03-20 19:05:15 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-20 19:17:06 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.025 |  |
| 2026-03-20 19:05:27 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.029 |  |
| 2026-03-20 19:42:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.036 |  |
| 2026-03-20 19:00:22 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.041 |  |
| 2026-03-20 19:03:21 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.051 |  |
| 2026-03-20 19:36:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.063 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 19:03:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)