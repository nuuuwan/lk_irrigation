# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_08:05:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 08:05:48 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.048 |  |
| 2026-02-13 08:05:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:05:07 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:04:29 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 08:04:27 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-02-13 08:04:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:03:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:38 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:21 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.053 |  |
| 2026-02-13 08:03:13 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:03:04 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:59 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:22 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:17 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.181 |  |
| 2026-02-13 08:02:00 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-02-13 08:01:43 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.435 |  |
| 2026-02-13 08:01:42 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-13 08:00:57 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:00:45 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.051 |  |
| 2026-02-13 08:00:22 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:00:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-13 08:00:11 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 07:45:31 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 07:40:57 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.048 |  |
| 2026-02-13 07:22:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-13 07:19:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 07:08:54 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-13 08:01:42 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-13 07:04:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-13 07:45:31 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 07:03:25 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-13 08:00:16 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-13 07:01:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 08:04:29 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 08:03:13 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:04:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:00:57 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:00:11 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 07:07:34 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 07:05:53 | Dunamale (Aththanagalu Oya) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 08:02:00 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:04 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:59 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 07:22:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:38 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:17 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:02:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-13 07:07:30 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:05:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:05:07 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:00:22 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 08:04:27 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-02-13 07:01:54 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.011 |  |
| 2026-02-13 07:02:28 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-02-13 07:19:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.025 |  |
| 2026-02-13 08:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-02-13 08:05:48 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.048 |  |
| 2026-02-13 08:00:45 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.051 |  |
| 2026-02-13 08:03:21 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.053 |  |
| 2026-02-13 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.181 |  |
| 2026-02-13 08:01:43 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.435 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)