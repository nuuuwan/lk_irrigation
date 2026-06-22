# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_00:28:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 00:28:21 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 00:23:57 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:15:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-23 00:08:21 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 18.281 | 🔺 Rising |
| 2026-06-23 00:08:10 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-06-23 00:08:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-06-23 00:07:31 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-06-23 00:06:15 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:06:13 | Norwood (Kelani Ganga) | 0.00 | 🟢 Normal | 18.281 | 🔺 Rising |
| 2026-06-23 00:06:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:06:06 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:06:04 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-06-23 00:05:34 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:05:03 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | -0.135 |  |
| 2026-06-23 00:04:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 00:04:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-23 00:04:09 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 00:04:09 | Glencourse (Kelani Ganga) | 13.02 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-06-23 00:04:02 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-23 00:03:58 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:03:45 | Giriulla (Maha Oya) | 2.22 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-06-23 00:03:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:03:13 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-06-23 00:03:11 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-23 00:02:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-23 00:02:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:22 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 00:02:21 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:21 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.181 | 🔺 Rising |
| 2026-06-23 00:02:06 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-23 00:01:44 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-06-23 00:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:21 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:00:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:00:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 00:02:21 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.181 | 🔺 Rising |
| 2026-06-23 00:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-06-23 00:08:21 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 18.281 | 🔺 Rising |
| 2026-06-23 00:08:10 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-06-23 00:03:45 | Giriulla (Maha Oya) | 2.22 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-06-23 00:04:09 | Glencourse (Kelani Ganga) | 13.02 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-06-23 00:03:13 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-06-23 00:06:04 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-06-23 00:07:31 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-06-23 00:04:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-23 00:02:06 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-23 00:02:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-23 00:03:11 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-23 00:04:02 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-23 00:04:09 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 00:02:22 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 00:28:21 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 00:15:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-23 00:04:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 00:06:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:01:44 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:08:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:01:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:21 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:00:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:00:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:03:58 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:03:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:23:57 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:06:06 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:05:34 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:02:21 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 00:05:03 | Deraniyagala (Kelani Ganga) | 2.47 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)