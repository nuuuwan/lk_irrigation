# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_03:47:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 03:47:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:45:51 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 03:29:55 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-12 03:25:37 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-12 03:15:34 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.036 |  |
| 2026-06-12 03:14:26 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:14:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-06-12 03:12:45 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-12 03:11:56 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-12 03:09:56 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-06-12 03:07:02 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:06:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:06:38 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 03:06:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 03:06:21 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:05:40 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-12 03:05:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-12 03:05:21 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 03:05:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-12 03:04:57 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-06-12 03:03:53 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-06-12 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-06-12 03:03:40 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:03:34 | Rathnapura (Kalu Ganga) | 5.67 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-06-12 03:03:32 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:03:13 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -4.988 |  |
| 2026-06-12 03:03:12 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-12 03:03:11 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-12 03:03:04 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-12 03:02:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -4.988 |  |
| 2026-06-12 03:02:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-12 03:02:34 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:02:24 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:02:21 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-06-12 03:02:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:01:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-06-12 03:01:29 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | 0.443 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 03:03:34 | Rathnapura (Kalu Ganga) | 5.67 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-06-12 03:01:29 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-06-12 03:14:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-06-12 03:02:21 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-06-12 03:25:37 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-12 03:11:56 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-12 03:03:04 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-12 03:05:40 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-12 03:05:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-12 02:06:01 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 03:03:12 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-12 03:05:25 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-12 03:12:45 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-12 03:45:51 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 03:05:21 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 03:06:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 03:06:38 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 03:00:17 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 03:29:55 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-12 03:02:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-12 03:02:24 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:06:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:03:40 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:07:02 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:02:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:14:26 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:02:34 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:47:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:03:32 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:04:57 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-06-12 03:03:53 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-06-12 03:01:45 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-12 03:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-06-12 03:15:34 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.036 |  |
| 2026-06-12 03:09:56 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-06-12 03:03:13 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -4.988 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)