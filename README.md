# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_01:37:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,228 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 01:37:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:31:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:27:55 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-04-25 01:21:04 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-04-25 01:20:11 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-04-25 01:15:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-04-25 01:08:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 21.545 | 🔺 Rising |
| 2026-04-25 01:08:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:07:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:07:31 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-04-25 01:06:34 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 21.545 | 🔺 Rising |
| 2026-04-25 01:06:22 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:05:51 | Katharagama (Menik Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-04-25 01:05:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:05:11 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.049 |  |
| 2026-04-25 01:04:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:04:22 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:03:50 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.153 |  |
| 2026-04-25 01:03:45 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:03:42 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.029 |  |
| 2026-04-25 01:03:17 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.123 |  |
| 2026-04-25 01:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 01:02:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-25 01:02:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.023 |  |
| 2026-04-25 01:01:45 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:01:37 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 01:01:31 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:00:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 01:08:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 21.545 | 🔺 Rising |
| 2026-04-25 01:02:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-25 01:00:27 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-25 01:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 01:01:37 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 01:08:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:01:45 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:05:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:07:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:06:22 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:04:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:03:45 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:31:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:21:04 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-04-25 01:15:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-04-25 01:05:51 | Katharagama (Menik Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-04-25 01:00:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:04:22 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:01:31 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:37:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-24 23:02:23 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-04-25 01:20:11 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-04-25 01:27:55 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-04-25 01:02:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.023 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 01:03:42 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.029 |  |
| 2026-04-25 00:03:15 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-04-25 00:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2026-04-25 01:05:11 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.049 |  |
| 2026-04-25 01:07:31 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-04-25 01:03:17 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.123 |  |
| 2026-04-25 01:03:50 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.153 |  |
| 2026-04-24 22:17:29 | Wellawaya (Kirindi Oya) | 0.18 | 🟢 Normal | -8.018 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)