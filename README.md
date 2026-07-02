# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_02:29:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,734 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 02:29:19 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-03 02:20:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 4.037 | 🔺 Rising |
| 2026-07-03 02:18:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 4.037 | 🔺 Rising |
| 2026-07-03 02:10:20 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-07-03 02:09:22 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 02:09:16 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:09:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:08:00 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.081 |  |
| 2026-07-03 02:06:24 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:06:05 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:06:04 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:05:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.022 |  |
| 2026-07-03 02:04:51 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:43 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:12 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -198.000 |  |
| 2026-07-03 02:04:10 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -198.000 |  |
| 2026-07-03 02:04:09 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -198.000 |  |
| 2026-07-03 02:04:08 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:44 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-03 02:03:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:17 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:14 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:02:49 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:02:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:02:02 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-07-03 02:01:48 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-03 02:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:01:34 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:58 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:51 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:32 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 02:20:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 4.037 | 🔺 Rising |
| 2026-07-03 02:03:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-03 01:23:15 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-03 02:09:22 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 01:05:22 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-03 02:01:48 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-03 02:29:19 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-03 02:04:51 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:32 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:58 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:02:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:09:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:02:49 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:51:05 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 01:41:22 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:08 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:44 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 00:59:47 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:00:51 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:06:24 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:06:05 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:03:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:43 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:04:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:51:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:09:16 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 01:02:33 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 01:04:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 01:03:43 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 01:07:25 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-03 02:02:02 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-07-03 02:10:20 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-07-02 20:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-07-03 02:05:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.022 |  |
| 2026-07-03 02:08:00 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.081 |  |
| 2026-07-03 02:04:12 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -198.000 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)