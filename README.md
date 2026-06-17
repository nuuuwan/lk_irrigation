# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_23:02:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 23:02:39 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.005 |  |
| 2026-06-17 23:01:26 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:23 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-06-17 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-06-17 23:01:13 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:06 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:00:39 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:00:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 22:50:31 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 22:16:46 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 22:13:52 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-06-17 22:13:29 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-06-17 22:12:43 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-17 22:12:34 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 23:01:23 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-06-17 22:02:54 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-06-17 22:02:56 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-06-17 22:13:29 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-06-17 22:12:43 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-17 21:03:29 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-17 22:06:22 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-17 22:03:37 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-17 22:02:05 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-17 22:06:36 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-17 22:10:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-17 22:06:58 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 23:01:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.005 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:07:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:00:39 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:06 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:26 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:39 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 22:06:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 22:02:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:13 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 22:13:52 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.008 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 22:03:19 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 23:00:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-06-17 22:07:25 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-06-17 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.022 |  |
| 2026-06-17 22:05:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-06-17 22:12:34 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |
| 2026-06-17 22:06:03 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.049 |  |
| 2026-06-17 22:05:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.101 |  |
| 2026-06-17 22:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.128 |  |
| 2026-06-17 22:03:49 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)