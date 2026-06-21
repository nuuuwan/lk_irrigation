# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_20:37:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 20:37:37 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:16:43 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.008 |  |
| 2026-06-21 20:10:23 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-06-21 20:09:54 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:08:43 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-21 20:08:02 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-21 20:07:24 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:05:21 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 3.765 | 🔺 Rising |
| 2026-06-21 20:04:59 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 20:04:51 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:04:08 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-21 20:03:56 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:42 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 20:03:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-21 20:03:28 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:28 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:18 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.069 |  |
| 2026-06-21 20:03:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.065 |  |
| 2026-06-21 20:02:37 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 20:02:37 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:34 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:19 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-06-21 20:02:16 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 20:05:21 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 3.765 | 🔺 Rising |
| 2026-06-21 20:01:16 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-06-21 20:02:19 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-06-21 20:08:43 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 20:03:31 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-21 20:04:08 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-21 20:08:02 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-21 20:02:14 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 20:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 20:02:37 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 20:03:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 20:00:08 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:01:15 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:04:51 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:01:54 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:37:37 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:37 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:34 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:08 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:28 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:42 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 19:46:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:00:47 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:02:12 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:07:24 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:01:45 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:03:28 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 20:16:43 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.008 |  |
| 2026-06-21 20:10:23 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-06-21 20:04:59 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 20:02:16 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-06-21 20:03:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.065 |  |
| 2026-06-21 20:03:18 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)