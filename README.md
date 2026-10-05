# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_14:26:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 14:26:05 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.036 |  |
| 2026-10-05 14:17:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:08:19 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2026-10-05 14:06:42 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:06:37 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.026 |  |
| 2026-10-05 14:06:31 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-10-05 14:06:16 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:06:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:05:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:05:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2026-10-05 14:05:35 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.041 |  |
| 2026-10-05 14:05:25 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.145 |  |
| 2026-10-05 14:05:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:05:18 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.080 |  |
| 2026-10-05 14:05:03 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.080 |  |
| 2026-10-05 14:04:57 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-05 14:04:56 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.028 |  |
| 2026-10-05 14:04:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:04:27 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.051 |  |
| 2026-10-05 14:04:24 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 14:03:53 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:03:35 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.099 |  |
| 2026-10-05 14:03:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:03:26 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:03:18 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:02:58 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 14:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.090 |  |
| 2026-10-05 14:02:09 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-10-05 14:02:09 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.110 |  |
| 2026-10-05 14:01:53 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 14:00:51 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-05 14:04:24 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 14:00:35 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 14:02:58 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 14:06:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:00:46 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:03:26 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:06:16 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:04:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:03:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:17:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-05 14:05:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:03:53 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:01:16 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:06:42 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:00:11 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:05:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-05 14:06:31 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-10-05 14:04:57 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-05 14:01:53 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:01:00 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:03:18 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:00:53 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-10-05 14:06:37 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.026 |  |
| 2026-10-05 14:04:56 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.028 |  |
| 2026-10-05 14:08:19 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2026-10-05 14:26:05 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.036 |  |
| 2026-10-05 14:02:09 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-10-05 14:05:35 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.041 |  |
| 2026-10-05 14:05:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2026-10-05 14:04:27 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.051 |  |
| 2026-10-05 14:05:03 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.080 |  |
| 2026-10-05 14:05:18 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.080 |  |
| 2026-10-05 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.090 |  |
| 2026-10-05 14:03:35 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.099 |  |
| 2026-10-05 14:02:09 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.110 |  |
| 2026-10-05 14:05:25 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)