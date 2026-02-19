# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_04:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 04:10:34 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.055 |  |
| 2026-02-20 04:08:25 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-20 04:05:25 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:05:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:48 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:26 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 04:04:15 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-20 04:04:03 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-20 04:03:56 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.194 |  |
| 2026-02-20 04:03:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:31 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:12 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:02:53 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-20 04:02:33 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-20 04:02:03 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 04:02:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.130 |  |
| 2026-02-20 04:01:46 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:01:41 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:01:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 04:01:05 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:00:53 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:00:52 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:00:23 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-20 03:28:41 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 864.000 | 🔺 Rising |
| 2026-02-20 03:06:57 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.497 | 🔺 Rising |
| 2026-02-20 03:05:47 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-02-20 04:00:23 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-20 04:04:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-20 04:02:33 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-20 04:04:26 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 04:02:03 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 04:01:05 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 04:08:25 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-20 04:01:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 04:00:52 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 03:01:48 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:01:46 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 23:12:07 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:15 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-20 03:09:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:05:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-20 03:04:13 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-20 03:02:42 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:31 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:48 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:05:25 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 03:04:49 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:00:53 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:01:41 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:04:03 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-20 04:02:53 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-20 03:03:46 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.025 |  |
| 2026-02-20 04:10:34 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.055 |  |
| 2026-02-20 03:03:32 | Padiyathalawa (Maduru Oya) | 3.25 | 🟢 Normal | -0.122 |  |
| 2026-02-20 04:02:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.130 |  |
| 2026-02-20 04:03:56 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)