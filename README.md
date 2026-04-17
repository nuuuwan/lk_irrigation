# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_09:31:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 09:31:46 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:15:05 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:13:48 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.036 |  |
| 2026-04-17 09:08:52 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:08:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-04-17 09:08:02 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-17 09:06:34 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:06:25 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.051 |  |
| 2026-04-17 09:05:58 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:05:25 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:04:54 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-17 09:04:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:03:37 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:03:29 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.407 |  |
| 2026-04-17 09:03:29 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:03:13 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.059 |  |
| 2026-04-17 09:03:09 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-17 09:02:54 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.075 |  |
| 2026-04-17 09:02:50 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:02:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:23 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:14 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.099 |  |
| 2026-04-17 09:02:08 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.070 |  |
| 2026-04-17 09:02:08 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:02:02 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-17 09:01:59 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 09:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:54 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:19 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:01:12 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:04 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-04-17 09:00:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:00:11 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 09:03:09 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-17 09:04:54 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-17 09:08:02 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-17 09:01:59 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:08 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:31:46 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:23 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:54 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:03:13 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:06:34 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:00:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:01:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:05:25 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:04:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:15:05 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-17 09:02:08 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:01:19 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:03:29 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:00:11 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-04-17 09:02:02 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-17 09:01:04 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-04-17 09:08:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-04-17 09:05:58 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:02:50 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:03:37 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-04-17 09:13:48 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.036 |  |
| 2026-04-17 09:06:25 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.051 |  |
| 2026-04-17 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.059 |  |
| 2026-04-17 09:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.070 |  |
| 2026-04-17 09:02:54 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.075 |  |
| 2026-04-17 09:02:14 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.099 |  |
| 2026-04-17 09:03:29 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.407 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)