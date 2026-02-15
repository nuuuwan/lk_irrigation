# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_08:06:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 08:06:02 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-15 08:05:11 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-15 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-02-15 08:04:35 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:04:15 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-15 08:04:07 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.042 |  |
| 2026-02-15 08:04:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:54 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-15 08:03:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:29 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:03:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:19 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.048 |  |
| 2026-02-15 08:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.057 |  |
| 2026-02-15 08:03:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:02:58 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-15 08:02:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:02:30 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:02:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.179 |  |
| 2026-02-15 08:02:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:49 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:46 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:45 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | -0.162 |  |
| 2026-02-15 08:01:45 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 08:01:37 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:31 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.218 |  |
| 2026-02-15 08:01:25 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-15 08:01:10 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:00:49 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:00:30 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.073 |  |
| 2026-02-15 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:38:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.014 |  |
| 2026-02-15 07:35:01 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-02-15 07:14:58 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:14:46 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:14:19 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.018 |  |
| 2026-02-15 07:13:26 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-02-15 07:12:47 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-02-15 07:10:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 08:02:58 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-15 08:01:45 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 08:03:29 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:04:35 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 08:02:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:02:30 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:46 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:10 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:07:00 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:04:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:00:49 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:04:37 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 07:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:37 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:02:53 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:01:49 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:06:02 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-15 08:01:25 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-15 07:38:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.014 |  |
| 2026-02-15 07:14:19 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.018 |  |
| 2026-02-15 08:03:54 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-15 08:04:15 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-15 08:05:11 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-15 07:02:29 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-15 08:04:07 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.042 |  |
| 2026-02-15 08:03:19 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.048 |  |
| 2026-02-15 08:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.057 |  |
| 2026-02-15 08:05:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-02-15 08:00:30 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.073 |  |
| 2026-02-15 08:01:45 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | -0.162 |  |
| 2026-02-15 08:02:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.179 |  |
| 2026-02-15 07:01:51 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.198 |  |
| 2026-02-15 08:01:31 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)