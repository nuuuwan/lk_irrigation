# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_09:07:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,113 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 09:07:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:07:21 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:06:58 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:06:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:06:18 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:06:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:05:21 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:05:02 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:04:39 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:04:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:04:21 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.014 |  |
| 2026-03-01 09:04:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-03-01 09:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.071 |  |
| 2026-03-01 09:03:28 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.271 |  |
| 2026-03-01 09:03:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:03:22 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:03:11 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.103 |  |
| 2026-03-01 09:03:00 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-01 09:02:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:02:42 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-01 09:02:32 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:02:29 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-01 09:02:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:02:01 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:59 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:37 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-03-01 09:01:35 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 09:01:22 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:00:53 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-01 09:00:10 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-01 08:59:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:26:34 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:21:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.071 |  |
| 2026-03-01 08:21:15 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.014 |  |
| 2026-03-01 08:13:02 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 09:03:00 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-01 09:02:42 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-01 09:01:35 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 09:02:32 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:06:18 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:06:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:05:02 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:07:21 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 09:02:01 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:02:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:04:39 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:07:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:05:21 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:12 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:26:34 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:04:20 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:03:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:59:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:13:02 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:06:58 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:22 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:04:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:02:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:06:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:08:35 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:59 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 09:01:37 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-03-01 09:00:10 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-01 09:00:53 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-01 09:02:29 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-01 09:04:21 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.014 |  |
| 2026-03-01 08:08:39 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-03-01 08:02:10 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-03-01 09:04:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-03-01 09:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.071 |  |
| 2026-03-01 09:03:11 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.103 |  |
| 2026-03-01 09:03:28 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)