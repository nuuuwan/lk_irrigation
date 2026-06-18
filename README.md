# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_13:01:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,693 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 13:01:25 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:01:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:01:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-18 13:01:08 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:00:58 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:00:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-18 13:00:12 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-06-18 12:27:17 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-06-18 12:15:57 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:12:35 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 13:01:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-18 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.33 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-18 12:03:37 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-18 12:05:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-18 12:02:58 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 12:04:25 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-18 12:00:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 12:06:14 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 12:04:34 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 12:05:56 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:01:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:01:25 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:01:13 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:00:58 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:02:45 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:03:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:01:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:03:05 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:05:31 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:01:19 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:01:08 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:00:03 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:02:14 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 12:02:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-06-18 12:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-18 13:00:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-18 12:01:09 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-18 12:27:17 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-06-18 13:00:12 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-06-18 12:04:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.029 |  |
| 2026-06-18 12:05:48 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-06-18 12:12:35 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.043 |  |
| 2026-06-18 12:02:22 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.048 |  |
| 2026-06-18 12:05:51 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.053 |  |
| 2026-06-18 12:02:39 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.059 |  |
| 2026-06-18 12:09:37 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.062 |  |
| 2026-06-18 12:04:38 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)