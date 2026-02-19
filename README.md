# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_18:40:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,508 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 18:40:18 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 18:29:05 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:25:33 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:09:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 18:08:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:07:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:07:11 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-19 18:07:06 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 18:07:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-19 18:06:38 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:06:30 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-19 18:06:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:05:24 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-02-19 18:04:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:36 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-19 18:04:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-19 18:04:17 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:15 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 18:04:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:48 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 18:03:35 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 18:03:15 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:58 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:52 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:44 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:43 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:33 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 18:04:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-02-19 18:04:36 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-19 18:09:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 18:07:06 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 18:07:11 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-19 18:06:30 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-19 18:03:35 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 18:04:15 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 18:03:40 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 18:40:18 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 18:07:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-19 18:03:48 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 18:08:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:29:05 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:15 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:17 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:06:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:50 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:44 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:58 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:25:33 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:07:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:19 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:43 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:06:38 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:33 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:04:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:02:52 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:05:24 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-02-19 18:02:09 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-02-19 18:01:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.091 |  |
| 2026-02-19 18:01:54 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)