# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_09:18:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,144 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 09:18:38 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-22 09:13:01 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-22 09:12:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:08:44 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 09:07:07 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-22 09:06:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-22 09:06:14 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 09:06:03 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 09:05:40 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-22 09:05:37 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-06-22 09:04:59 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-22 09:04:58 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-22 09:04:51 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:18 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-22 09:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-22 09:04:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:04:00 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-22 09:04:00 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-22 09:03:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:03:16 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:03:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-06-22 09:02:56 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:43 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:28 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-06-22 09:02:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:02:13 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:02:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-22 09:01:35 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-22 09:01:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-06-22 09:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:01:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 09:01:10 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:00:48 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:00:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 09:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-22 09:02:28 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-06-22 08:14:42 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-22 09:05:37 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-06-22 09:13:01 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-22 09:04:59 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-22 09:05:40 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-22 09:04:00 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-22 09:07:07 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-22 09:08:44 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 09:18:38 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-22 09:04:00 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-22 09:04:58 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-22 09:06:14 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 09:04:18 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-22 09:01:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 09:06:03 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 09:02:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-22 09:06:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-22 09:01:35 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-22 09:02:13 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:04:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:02:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:12:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 09:00:48 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:01:10 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:56 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:00:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:03:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:43 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:02:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:03:16 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:04:51 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 09:03:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-06-22 09:01:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)