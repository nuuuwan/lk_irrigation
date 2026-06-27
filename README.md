# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_05:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 05:17:20 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-27 05:16:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-06-27 05:12:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:09:38 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-27 05:08:59 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:08:14 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:06:34 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:06:29 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-27 05:05:50 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-06-27 05:05:22 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:05:05 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -108.000 |  |
| 2026-06-27 05:05:04 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -108.000 |  |
| 2026-06-27 05:04:43 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.180 |  |
| 2026-06-27 05:04:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.078 |  |
| 2026-06-27 05:04:40 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.039 |  |
| 2026-06-27 05:04:26 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 05:04:14 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:03:31 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:03:14 | Dunamale (Aththanagalu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-27 05:03:09 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:02:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-27 05:02:26 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:02:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-06-27 05:02:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-27 05:01:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:24 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-06-27 05:01:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:11 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-06-27 05:01:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-27 04:51:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 05:02:35 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-27 05:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-27 05:06:29 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-27 05:01:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-27 04:01:02 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 05:17:20 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-27 05:04:26 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:08:14 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:12:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:04:14 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:03:09 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 04:13:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:13:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:05:22 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:09:38 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:02:26 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:03:31 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:08:59 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:06:34 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:01:24 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-06-27 05:01:11 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-06-27 04:23:17 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-06-27 05:02:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-27 05:03:14 | Dunamale (Aththanagalu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-27 04:28:27 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.015 |  |
| 2026-06-27 04:08:54 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-06-27 05:02:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-06-27 05:05:50 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-06-27 05:04:40 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.039 |  |
| 2026-06-27 05:16:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-06-27 05:04:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.078 |  |
| 2026-06-27 05:04:43 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.180 |  |
| 2026-06-27 05:05:05 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)