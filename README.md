# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_07:39:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 07:39:29 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:34:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-21 07:17:27 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:15:42 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:10:32 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-21 07:09:19 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.267 |  |
| 2026-06-21 07:08:36 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:08:31 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-06-21 07:08:00 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-06-21 07:06:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-21 07:05:58 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:45 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-06-21 07:05:38 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:32 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:21 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 07:05:16 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 07:10:32 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-21 07:34:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-21 07:00:55 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-21 07:05:21 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 07:02:41 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:00:56 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:08:36 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:00:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:00:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:15:42 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:39:29 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:04:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:03:31 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:04:35 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:38 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:20 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:58 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:02:43 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:17:27 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:04:03 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:05:32 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:31 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 07:01:51 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.002 |  |
| 2026-06-21 07:08:00 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-06-21 07:05:16 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-06-21 07:06:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-21 07:04:33 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-06-21 07:05:45 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-06-21 07:08:31 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-06-21 07:02:34 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.031 |  |
| 2026-06-21 07:00:18 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.062 |  |
| 2026-06-21 07:03:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.222 |  |
| 2026-06-21 07:09:19 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.267 |  |
| 2026-06-21 06:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.671 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)