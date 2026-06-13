# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_13:21:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,278 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 13:21:19 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-06-13 13:19:41 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:08:24 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.064 |  |
| 2026-06-13 13:08:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:07:20 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:07:11 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:07:07 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:06:57 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 13:06:53 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-06-13 13:06:06 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 13:05:56 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:05:53 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:05:45 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-06-13 13:05:28 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:05:23 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.062 |  |
| 2026-06-13 13:05:08 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:05:05 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-06-13 13:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-13 13:04:24 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 13:03:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:25 | Galgamuwa (Mee Oya) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-06-13 13:03:17 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:03 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-06-13 13:03:03 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.096 |  |
| 2026-06-13 13:02:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-13 13:02:39 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 13:02:30 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 13:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:02:14 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-13 13:02:13 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 13:02:09 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2026-06-13 13:02:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:02:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:01:38 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.071 |  |
| 2026-06-13 13:01:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:01:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:01:28 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 13:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-13 13:06:06 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.000 |  |
| 2026-06-13 13:01:38 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.071 |  |
| 2026-06-13 13:03:03 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.096 |  |
| 2026-06-13 13:02:39 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 13:06:57 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 13:02:30 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 13:02:13 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 13:04:24 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 13:05:56 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:01:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:01:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 13:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:05:08 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:02:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:17 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:07:11 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:05:53 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:03:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:08:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:19:41 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:07:20 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 13:21:19 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-06-13 13:02:14 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-13 13:02:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-13 13:07:07 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:01:28 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:05:28 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-06-13 13:03:25 | Galgamuwa (Mee Oya) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-06-13 13:05:05 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-06-13 13:06:53 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-06-13 13:02:09 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2026-06-13 13:03:03 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-06-13 12:13:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.039 |  |
| 2026-06-13 13:05:45 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.048 |  |
| 2026-06-13 13:05:23 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.062 |  |
| 2026-06-13 13:08:24 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)